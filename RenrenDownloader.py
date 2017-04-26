#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#
# update 2017/04/26 by liegu.petesky
# https://github.com/liegu
import ConfigParser
import string

from Renren import SuperRenren

def main():

    cf = ConfigParser.ConfigParser()
    cf.read("user.txt")
    try:
        #账户
        cookie =   cf.get("conf", "cookie")
        threadnumber=string.atoi(cf.get("conf", "threadnumber"))
    except:
        pass

    renren = SuperRenren()
    if renren.CreateByCookie(cookie):

       renren.DownloadAllFriendsAlbums(threadnumber=threadnumber)
    
if __name__ == '__main__':
    main()
    
