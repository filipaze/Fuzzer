#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Author: Filipe Azevedo

import random
import hashlib
import requests
import json
import argparse
import sys
from urllib.parse import urlparse
import base64
import os
from contextlib import redirect_stdout

if sys.version_info < (3, 7):
    sys.stdout.write("Sorry, fuzzer requires Python 3.7 or higher\n")
    sys.exit(1)

def appendStrings(strings):
    str = ""
    for item in strings:
        str = str + item
    return str


def prints_results(print_results_method,print_results_url,print_results_wordlist,print_results_output,print_results_timeout,print_matchResponseCode,match_responseSize):

    print("________________________________________________                               \n",
          "                                                                               \n",
          " :: Method             : ",print_results_method,                              "\n",
          " :: URL                : ",print_results_url,                                 "\n",
          " :: Wordlist           : ",print_results_wordlist,                            "\n",
          " :: Output             : ",print_results_output,                              "\n",
          " :: Timeout            : ",print_results_timeout,                             "\n",
          " :: Matcher            :  Response status: ",print_matchResponseCode,         "\n",
          " :: Matcher            :  Response status: ",match_responseSize,              "\n",
          "________________________________________________                               \n")



def output_to_file_normal(WORD,FUZZER,content_length,response_code_show):

    var_output_to_file_normal = (""+"{:<25}".format(WORD)+" | "+"{:<25}".format(FUZZER)+" [ Response Code: "+response_code_show+", Size: "+ content_length+ " ]"+"\n")
    str = appendStrings(var_output_to_file_normal)
    output_file.write(str)


def output_to_file_request_complete(WORD,FUZZER,payload_show):

    var_output_to_file_normal = ("\n\nWORD: "+WORD+" | HASH: "+FUZZER+"\n\nHEADERS:\n\n"+payload_show+"\n\n")
    str = appendStrings(var_output_to_file_normal)
    output_file.write(str)


def output_to_file_response_complete(response_headers_show,content_show,response_code_show):

    var_output_to_file_normal = ("\nRESPONSE CODE: "+response_code_show+"\n\n"+response_headers_show+"\n"+"RESPONSE:\n\n "+content_show+"\n\n\n-----------------------------------------------------\n\n")
    str = appendStrings(var_output_to_file_normal)
    output_file.write(str)


def request(FUZZER,WORD,url_target,match_responseSize):



    if not args.headers:
        payload={}
        url_target = url_target.replace("FUZZER",FUZZER)
    else:
        payload = args.headers
        url_target = url_target.replace("FUZZER",FUZZER)
        url_target = url_target.replace("FUZZER",FUZZER)
        payload=payload.replace("FUZZER",FUZZER)
        payload_show=payload
        payload_show = payload_show.replace("\",","\",\n")
        payload_show = payload_show.replace("{","")
        payload_show = payload_show.replace("}","")
        payload_show = payload_show.replace("\"","")

    if (args.method=="POST"):
        body={}
        headers = args.body

# -------------------------------------------------------------------------------------------------
        r = requests.post(url_target, data=json.dumps(payload),headers=body, timeout=timeout)
# -------------------------------------------------------------------------------------------------

    else:

        args.method=="GET"

# -------------------------------------------------------------------------------------------------
        r = requests.get(url_target, data=json.dumps(payload))
# -------------------------------------------------------------------------------------------------

    content_length = str(len(r.content))

    content_show = r.content
    content_show= content_show.decode("utf-8")
    content_show= content_show.replace("\\n","\\n")
    content_show= content_show.replace("\\n","\\n")

    response_headers = r.content
    response_headers_show=str(r.headers)
    response_code_show = str(r.status_code)

    if not args.matchResponseSize:
        match_responseSize=content_length



    if response_code_show in response_code_matcher and content_length==match_responseSize:

        print("","{:<25}".format(WORD)," | ","{:<25}".format(FUZZER), " [ Response Code: ",response_code_show,", Size: ", content_length, " ]")

    if output_to_file==True:

        if args.verbose:

                output_to_file_request_complete(WORD,FUZZER,payload_show)
                output_to_file_response_complete(response_headers_show,content_show,response_code_show)

        else:
            output_to_file_normal(WORD,FUZZER,content_length,response_code_show)



# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------


print("\n\n      ___      ___         ___         ___         ___         ___   \n"
          "     /  /\    /__/\       /  /\       /  /\       /  /\       /  /\        \n"
          "    /  /:/_   \  \:\     /  /::|     /  /::|     /  /:/_     /  /::\       \n"
          "   /  /:/ /\   \  \:\   /  /:/:|    /  /:/:|    /  /:/ /\   /  /:/\:\      \n"
          "  /  /:/ /:___  \  \:\ /  /:/|:|__ /  /:/|:|__ /  /:/ /:/_ /  /:/~/:/      \n"
          " /__/:/ /:/__/\  \__\:/__/:/ |:| //__/:/ |:| //__/:/ /:/ //__/:/ /:/___    \n"
          " \  \:\/:/\  \:\ /  /:\__\/  |:|/:\__\/  |:|/:\  \:\/:/ /:\  \:\/:::::/    \n"
          "  \  \::/  \  \:\  /:/    |  |:/:/    |  |:/:/ \  \::/ /:/ \  \::/~~~~     \n"
          "   \  \:\   \  \:\/:/     |  |::/     |  |::/   \  \:\/:/   \  \:\         \n"
          "    \  \:\   \  \::/      |  |:/      |  |:/     \  \::/     \  \:\        \n"
          "     \__\/    \__\/       |__|/       |__|/       \__\/       \__\/        \n"
          "\n   © Filipe Azevedo | filipaze.com   v1.0.0                                \n")

parser = argparse.ArgumentParser(prog='tool',
  formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=65))

parser.add_argument("-w", "--wordlist",type=str, help="Wordlist file path",required=True)
parser.add_argument("-u", "--url", type=str, help="Target URL", required=True)
parser.add_argument("-d", "--headers", type=str,help="Headers data. Use FUZZER for define the brute force location")
parser.add_argument("-e", "--encoding", type=str,help="Encoding: md5 | base64\nTo define the test case for ffuf, use the keyword FUZZER anywhere in the DATA payload.\n\n")
parser.add_argument("-o", "--output", type=str,help="Write output to file\n\n")
parser.add_argument("-X", "--method", type=str,help="HTTP method to use. Default is POST\n\n")
parser.add_argument("-b", "--body", type=str,help="Body data POST Request\n\n")
parser.add_argument("-t", "--timeout", type=str,help="Request timeout in seconds. Default is 3 seconds\n\n")
parser.add_argument("-mc", "--matchResponseCode", type=str,help="Match HTTP status codes (default: 200,204,301,302,307,401,403,405)\n\n")
parser.add_argument("-ms", "--matchResponseSize", type=str,help="Match HTTP response size\n\n")
parser.add_argument("-v", "--verbose",help="Verbose output. Printing full request and response. Default: False. Usage: -v 1 to activate")


args = parser.parse_args()

url_target = args.url

match_responseSize=""

if args.matchResponseSize:
    match_responseSize = str(args.matchResponseSize)

else:

    match_responseSize = "ALL"

#RULES

# YOU ARE OBLIGATED TO ADD OUTPUT FLAG WHEN VERBOSE IS ACTIVATE.
if args.verbose and not args.output:
    print("VERBOSE defined but not OUTPUT. YOU ARE OBLIGATED TO ADD OUTPUT FLAG WHEN VERBOSE IS ACTIVATE.\n")
    exit()


response_code_matcher = ["200", "204", "301", "302", "307", "400", "401", "402", "405"];


if args.matchResponseCode:
    response_code_matcher = args.matchResponseCode
    response_code_matcher = response_code_matcher.split(",")

timeout=10

if args.timeout:

    timeout=float(args.timeout)

if args.encoding:

    if (args.encoding!="md5" and args.encoding!="base64"):
        print("\nEncoding not defined. \n\nUsage:\n\npython3 hasher.py -w /home/wordlist.txt -u https://example.org/ -d '{\"Host\": DOMAIN,\"Connection\": \"close\",\"Cookie\": \"FUZZER\"}' -t md5\n\n")
        exit()

if args.headers:
    if ("FUZZER" not in args.headers and "DOMAIN" not in args.headers):
        print("\FUZZER defined but not use. \n\nUsage:\n\npython3 hasher.py -w /home/wordlist.txt -u https://example.org/ -d '{\"Host\": \"example.org\",\"Connection\": \"close\",\"Cookie\": \"FUZZER\"}' -t md5\n\n")
        exit()

print("\n\nUsage:\n\npython3 hasher.py -w /home/wordlist.txt -u https://example.org/ -d '{\"Host\": DOMAIN,\"Connection\": \"close\",\"Cookie\": \"FUZZER\"}' -t md5\n")
print("Encoding worlist...")
print("Sending requests...")

output_to_file = False

if args.output:
    output_path = args.output
    output_file = open(output_path, "w")
    output_to_file = True

else:
    args.output = "-"
    output_path = str(os.path.abspath(os.getcwd())+"/hasher_output.txt")

if args.body and args.method=="POST":
    body = {}

elif args.body:
    print("You can only use the -d option on POST request")
    exit()


wordlist_path = args.wordlist



print_results_method    = str(args.method)
print_results_url       = str(args.url)
print_results_wordlist  = str(args.wordlist)
print_results_output    = str(args.output)
print_results_timeout   = str(args.timeout)
print_matchResponseCode = response_code_matcher

if args.method:
    print_results_method = str(args.method)
else:
    print_results_method = "POST"

prints_results(print_results_method,print_results_url,print_results_wordlist,print_results_output,print_results_timeout,print_matchResponseCode,match_responseSize)



with open(wordlist_path,'r') as file:
    number_of_lines=0

    for line in file:

        number_of_lines += 1

        for word in line.split():


            if (args.encoding=="md5"):

                result = hashlib.md5(word.encode())
                request(result.hexdigest(),word,url_target,match_responseSize)

            elif (args.encoding=="base64"):


                message_bytes = word.encode('ascii')
                result = base64.b64encode(message_bytes)
                result= result.decode("utf-8")

                request(result, word, url_target,match_responseSize)

            else:
                request(word, word, url_target,match_responseSize)
