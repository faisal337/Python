# Page function to follow the FIFO Logic
def page(cache, request):
# First if loop to see if the request is not in the cache
    if request == 0 or request  == 'Q':
        pass
    elif request not in cache:
        requests.append(request)
        if len(cache) < 8:
            cache.append(request)
            print("Miss")
        else: 
            cache.pop(0)
            cache.append(request)
            print("Miss")
# Else if loop runs when the element is present in cache
    elif request in cache:
        print("Hit")
    return cache

# Initializing the cache
cache = []
# Intializing the requests list
requests = []
while True:
    request = input()
    if request == 'Q': 
        break
    elif request == '0':
        print(cache)
        requests = []
        cache = []
    else:
        request = int(request)
        page(cache, request)
print(cache)
print(requests)