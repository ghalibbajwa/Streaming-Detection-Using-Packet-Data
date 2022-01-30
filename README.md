        
                                                ,   ,                                
                                                $,  $,     ,                         
                                                "ss.$ss. .s'                         
                                        ,     .ss$$$$$$$$$$s,                        
                                        $. s$$$$$$$$$$$$$$`$$Ss                      
                                       "$$$$$$$$$$$$$$$$$$o$$$       ,              
                                      s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s               
                                      s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,             
                                      s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"             
                                     s$$$$$$$$$$'         `"""ss"$"$s""              
                                    s$$$$$$$$$$,              `"""""$  .s$$s        
                                    s$$$$$$$$$$$$s,...               `s$$'  `       
                                  `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-   
                                  `""""$$$$$$$$$$$$$$$$Ghalib###$$$$$$"     $.$'    
                                          "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|     
                                          "$$$$$$$$$$$Fasih$$$$$$$$$##s    .$$" $    
                                          $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `    
                                          $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'         
                                    ,   ,"     '  $$$$$$$$$$$$$$$$####s             
                                    $.          .s$$$$$$$$$$$$$$$$$####"            
                 ,                  "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"            
                    $                  .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"             
                          Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""              
                            "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"                  
                      ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'                      
                      $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,           
                    $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$            
                    "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$            
                    $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.         
                  $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.       
                  $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$      
                  $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
                  $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$' 
                  $$"$$$$$$$$$$$#####.$$$$$###'                .###$$$$$$$$$$"   
               _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$     
                    "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"     
                      ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"       
                      `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,       
                          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'    
                            $$$$$$$$$$$$$$$$$$$$$$$$S        '     
                              \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$                  
                                S$$$$$$$$$$$$$$$$$#"      $                         
                                 """""""""""""'      

# Part 1
- Traffic generated for a one hour long session on an android device using various multiple applications
- From android device, pcap captured for that session
- From android device, each flow in the pcap associated to the particular application that generated the traffic
# Part 2
- Traffic signature created for VoIP and Streaming applications
- Untagged pcap file ( raw pcap captured from android device) matched against the patterns to automatically identify VoIP and Streaming flows
This will require ML.
##  for part1 :
### Metadata will be extracted from every packet and the signature would be developed on the metadata

##  for part2:
### The metadata from the pcap will be extracted and signature would be matched.

# Domain
### Machine Learning
### Network Programing
### End User Monitoring

# Tools
### Wire Shark

# Hardware

### Android Device
### Windows PC/Laptop

# Programming Language
### python

# Useful Terms
### Flows
Packets having the same tuple belog to the same flows


# Use Case/End Goal

Over 60-70% of all Inernet Usage is of Streaming and VOIP. What if Inernet Service Providers can reduce their traffic load dramaticly just by targeting these two flows.
Detecting live streaming flows and reducing their size ( 1080p to 720 ) in realtime.


