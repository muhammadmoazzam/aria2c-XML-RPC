# What is aria2?
aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line. It supports HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink. https://aria2.github.io/

# Aria2c XML-RPC
Aria2 XML-RPC Methods for Python3 uses the xmlrpc.client library as suggested by [aria2c documentation](https://aria2.github.io/)

This allows very simple functions/methods offered by aria2c RPC interface using the Python classes and class methods. 
It provides some of the commonly used methdos provided by aria2c. 

It was mainly used for torrent handling provided by aria2c therefore the `addMagent()` function can also take in a normal URI for HTTP download and is not strictly used for manget uri.

For additional information about aria2c check the following links
- [aria2](https://aria2.github.io/)
- [aria2 Documentation (en)](https://aria2.github.io/manual/en/html/index.html)
- [RPC-Interface Methods](https://aria2.github.io/manual/en/html/aria2c.html#rpc-interface)


Pull requests are welcome ;)
