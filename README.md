
# Fuzzer (beta)  👋
A web fuzzer written in Python with something more. Beta version.

## Installation

```
git clone https://github.com/filipaze/Fuzzer.git; cd Fuzzer; python3 fuzzer.py -h
```
Fuzzer depends on python 3.7 or greater.

## Usage Examples

You can use Fuzzer as a fuzzing tool to find a directory, a subdomain, or anything that can be brute forced. But, the main reason I developed the tool was to have the ability to encode a string, then use it however you want, with no need to do previous encoding. Right now, it only accepts md5 and base64 but it will accept more in the future.

Typical fuzzing discovery by using the **FUZZER** keyword.
```
python3 fuzzer.py -u https://example.com -w /home/lists/wordlist.txt -d "{"Cookie":FUZZER}" -e md5
```
To write output to file use the **-o** flag. And the **-e** to define the encoding type.
```
python3 fuzzer.py -u https://example.com/FUZZER -w /home/lists/wordlist.txt -e md5 -o output.txt
```
To show only some status codes use **-mc=** and **-ms** for matching reponse sizes.
```
python3 fuzzer.py -u http://www.example.com/ -w /home/lists/top-usernames-shortlist.txt -d '{"Host": "www.example.com","Connection": "close","Content-Length": 129,"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5","Content-Type":"application/json","Accept": "*/*","Accept-Encoding": "gzip,deflate,sdch","Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4", "Cookie": FUZZER}' -o output.txt -v 1 -X POST -ms 1589 -mc 200
```
## Usage

```

      ___      ___         ___         ___         ___         ___   
     /  /\    /__/\       /  /\       /  /\       /  /\       /  /\        
    /  /:/_   \  \:\     /  /::|     /  /::|     /  /:/_     /  /::\       
   /  /:/ /\   \  \:\   /  /:/:|    /  /:/:|    /  /:/ /\   /  /:/\:\      
  /  /:/ /:___  \  \:\ /  /:/|:|__ /  /:/|:|__ /  /:/ /:/_ /  /:/~/:/      
 /__/:/ /:/__/\  \__\:/__/:/ |:| //__/:/ |:| //__/:/ /:/ //__/:/ /:/___    
 \  \:\/:/\  \:\ /  /:\__\/  |:|/:\__\/  |:|/:\  \:\/:/ /:\  \:\/:::::/    
  \  \::/  \  \:\  /:/    |  |:/:/    |  |:/:/ \  \::/ /:/ \  \::/~~~~     
   \  \:\   \  \:\/:/     |  |::/     |  |::/   \  \:\/:/   \  \:\         
    \  \:\   \  \::/      |  |:/      |  |:/     \  \::/     \  \:\        
     \__\/    \__\/       |__|/       |__|/       \__\/       \__\/        

   © Filipe Azevedo | filipaze.com   v1.0.0                                

usage: tool [-h] -w WORDLIST -u URL [-d HEADERS] [-e ENCODING] [-o OUTPUT] [-X METHOD] [-b BODY] [-t TIMEOUT] [-mc MATCHRESPONSECODE]
            [-ms MATCHRESPONSESIZE] [-v VERBOSE]

optional arguments:
  -h, --help                                                    show this help message and exit
  -w WORDLIST, --wordlist WORDLIST                              Wordlist file path
  -u URL, --url URL                                             Target URL
  -d HEADERS, --headers HEADERS                                 Headers data. Use FUZZER for define the brute force location
  -e ENCODING, --encoding ENCODING                              Encoding: md5 | base64. To define the test case for fuzzer, use the keyword FUZZER
                                                                anywhere in the DATA payload.
  -o OUTPUT, --output OUTPUT                                    Write output to file
  -X METHOD, --method METHOD                                    HTTP method to use. Default is POST
  -b BODY, --body BODY                                          Body data POST Request
  -t TIMEOUT, --timeout TIMEOUT                                 Request timeout in seconds. Default is 3 seconds
  -mc MATCHRESPONSECODE, --matchResponseCode MATCHRESPONSECODE  Match HTTP status codes (default: 200,204,301,302,307,401,403,405)
  -ms MATCHRESPONSESIZE, --matchResponseSize MATCHRESPONSESIZE  Match HTTP response size
  -v VERBOSE, --verbose VERBOSE                                 Verbose output. Printing full request and response. Default: False. Usage: -v 1 to
                                                                activate
```

## License

See [LICENSE](https://github.com/filipaze/Fuzzer/blob/main/LICENSE)

## Contact Me

You can ping me on [Twitter](https://twitter.com/filipaze_) or visit my [Website](https://www.filipaze.com/). 😀

