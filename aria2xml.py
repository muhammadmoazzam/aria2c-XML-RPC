import xmlrpc.client

class aria2:
    '''
    To specify the URL where RPC is listening use aria(url='http://host:port/')
    '''
    def __init__(self,secret=None,url='http://localhost:6800/rpc'):
        self.s = xmlrpc.client.ServerProxy(url)
        self.secret = secret

    def __convertTo(self,response,unit):
        '''
        Private Method to convert bytes to KB (Kilobytes), MB (MegaBytes) or GB (Gigabytes)
        '''
       
        if unit == 'MB':
            totalLength =None if response.get('totalLength') == None else round(((float(response.get('totalLength'))/1000))/1000,2)
            completedLength =None if response.get('completedLength') == None else round(((float(response.get('completedLength'))/1000))/1000,2)
            downloadSpeed =None if response.get('downloadSpeed') == None else round(((float(response.get('downloadSpeed'))/1000))/1000,2)
            uploadSpeed = None if response.get('uploadspeed') == None else round(((float(response.get('uploadSpeed'))/1000))/1000,2)
            response.update({
                'totalLength':(totalLength),
                'completedLength':(completedLength),
                'downloadSpeed':(downloadSpeed),
                'uploadSpeed':(uploadSpeed)
            })

        elif unit == 'KB':
            totalLength =None if response.get('totalLength') == None else round(float(response.get('totalLength'))/1000,2)
            completedLength =None if response.get('completedLength') == None else round(float(response.get('completedLength'))/1000,2)
            downloadSpeed =None if response.get('downloadSpeed') == None else round(float(response.get('downloadSpeed'))/1000,2)
            uploadSpeed = None if response.get('uploadspeed') == None else round(float(response.get('uploadSpeed'))/1000,2)

            response.update({
                'totalLength':(totalLength),
                'completedLength':(completedLength),
                'downloadSpeed':(downloadSpeed),
                'uploadSpeed':(uploadSpeed)
            })

        elif unit == 'GB':
            totalLength =None if response.get('totalLength') == None else round(((float(response.get('totalLength'))/1000)/1000)/1000,2)
            completedLength =None if response.get('completedLength') == None else round(((float(response.get('completedLength'))/1000)/1000)/1000,2)
            downloadSpeed =None if response.get('downloadSpeed') == None else round(((float(response.get('downloadSpeed'))/1000)/1000)/1000,2)
            uploadSpeed = None if response.get('uploadspeed') == None else round(((float(response.get('uploadSpeed'))/1000)/1000)/1000,2)
            
            response.update({
                'totalLength':(totalLength),
                'completedLength':(completedLength),
                'downloadSpeed':(downloadSpeed),
                'uploadSpeed':(uploadSpeed)
            })

        # Filtering/Removing all the None Items if any
        response = {k: v for k, v in response.items() if v is not None}

        return response
            
    def addMagnet(self,magnet):
        '''
        This method adds a new Bittorent download. uris is an array of BitTorrent URIs (strings) pointing to the same resource.
        '''
        if self.secret:
            response = self.s.aria2.addUri('token:'+self.secret,[magnet])
        else:
            response = self.s.aria2.addUri([magnet])
        self.status(response)
        return response

    def globalStatus(self,unit='MB'):
        '''
        '''
        if self.secret:
            response = self.s.aria2.getGlobalStat('token:'+self.secret)
        else:
            response = self.s.aria2.getGlobalStat()
        response = self.__convertTo(response,unit=unit)
        return response

    def remove(self,gid):
        '''
        This method removes the download denoted by gid (string). This method returns GID of removed download.
        '''
        if self.secret:
            response = self.s.aria2.remove('token:'+self.secret,gid)
        else:
            response = self.s.aria2.remove(gid)
        self.removeDownloadResult(response)
        return response

    def forceRemove(self,gid):
        '''
        This method removes the download denoted by gid. This method behaves just like self.remove() except that this method removes the download without performing any actions which take time, such as contacting BitTorrent trackers to unregister the download first.
        '''
        if self.secret:
            response = self.s.aria2.forceRemove('token:'+self.secret,gid)
        else:
            response = self.s.aria2.forceRemove(gid)
        self.removeDownloadResult(response)
        return response

    def pause(self,gid):
        '''
        This method pauses the download denoted by gid (string). The status of paused download
        '''
        if self.secret:
            response = self.s.aria2.pause('token:'+self.secret,gid)
        else:
            response = self.s.aria2.pause(gid)
        return response

    def resume(self,gid):
        '''
        This method moves paused download denoted by gid (string) to download waiting queue,
        '''
        if self.secret:
            response = self.s.aria2.unpause('token:'+self.secret,gid)
        else:
            response = self.s.aria2.unpause(gid)
        return response
    
    def resumeAll(self):
        '''
        This method is equal to calling resume() but for every paused download. This methods returns OK.
        '''
        if self.secret:
            response = self.s.aria2.unpauseAll('token:'+self.secret)
        else:
            response = self.s.aria2.unpauseAll()
        return response

    def activeDownloads(self,keys=["gid","status","totalLength","completedLength","downloadSpeed","uploadSpeed"],unit='MB'):
        '''
        This method returns a list of all active downloads. The response is an array of the same dictory key value pair as returned by the self.status() method. For the keys parameter, please refer to the self.status() method.
        '''
        if self.secret:
            response = self.s.aria2.tellActive('token:'+self.secret,keys)
        else:
            response = self.s.aria2.tellActive(keys)
        response = self.__convertTo(response,unit)
        return response


    def status(self,gid,keys=["gid","status","totalLength","completedLength","downloadSpeed","uploadSpeed"],unit='MB'):
        '''
        This method returns the progress of the download denoted by gid (string). keys is an array of strings. If specified, the response contains only keys in the keys array. If keys is empty or omitted, the response contains all keys. This is useful when you just want specific keys and avoid unnecessary transfers.\nFor example: self.status("2089b05ecca3d829", ["gid", "status"])
        \nThe response is a dictionary and contains key value pairs.
        \nSee list of all keys at https://aria2.github.io/manual/en/html/aria2c.html#aria2.tellStatus
        \nUnit specifies the return value up/down speed and 
        '''
        if self.secret:
            response = self.s.aria2.tellStatus('token:'+self.secret,gid,keys)
        else:
            response = self.s.aria2.tellStatus(gid,keys)
        response = self.__convertTo(response,unit=unit)
        return response

    def listAllStopped(self,offset=0,num=0,keys=["gid","status","totalLength","completedLength","downloadSpeed","uploadSpeed"],unit='MB'):
        '''
        
        '''
        if offset == 0 and num == 0:
            num = int(self.globalStatus()['numStoppedTotal'])
        if self.secret:
            response = self.s.aria2.tellStopped('token:'+self.secret,offset,num,keys)
        else:
            response = self.s.aria2.tellStopped(offset,num,keys)

        all_results = []
        for i in range(len(response)):
            all_results.append(self.__convertTo(response[i],unit=unit))
        return all_results
    
    def removeDownloadResult(self,gid):
        '''
        This private method removes a completed/error/removed download denoted by gid from memory. This method returns OK for success.
        '''
        if self.secret:
            self.s.aria2.removeDownloadResult('token:'+self.secret,gid)
        else:
            self.s.aria2.removeDownloadResult(gid)
    def shutdownAria(self):
        '''
        This method shuts down aria2. This method returns OK.
        '''
        if self.secret:
            self.s.aria2.shutdown('token:'+self.secret)
        else:
            self.s.aria2.shutdown()