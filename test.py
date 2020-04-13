import sys, getopt

def main(argv):
    num_runners = -1
    track_size = -1
    path = "X"
    loop = False
    runner_type = "default"
    
    try: 
        opts, args = getopt.getopt(argv,"ln:t:")
        
        for opt, arg in opts:
            if opt in ("-l"):
                loop = True
                print("loop="+str(loop))
            elif opt in ("-n"):
                num_runners = arg
                print("num_runners = "+str(num_runners))
            elif opt in ("-t"):
                track_size = arg
                print("track = "+ str(track_size))
    except:
        print("asi no xd")
    
    

    print("Sea cabo")
    
    
    
if __name__ == "__main__":

    main(sys.argv[1:])
