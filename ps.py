#      * *
#     *  * 
#        *
#        *
#    * * * * *


rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==mid or i==rows or i==1 and j==mid-1 or i==2 and j==i-1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


#      * * * * *
#              *
#      * * * * *
#      *
#      * * * * *
 
rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==mid or i==rows or (j==1 and i>=mid) or (j==rows and i<=mid): 
            res+="."+" "
        else:
            res+=" "+" "
    print(res)


#     * * * * 
#            *
#     * * * * 
#            *
#     * * * * 

rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if (i==1 and j!=rows) or (i==mid and j!=rows) or (i==rows and j!=rows) or (j==rows and i!=1 and i!=rows and i!=mid):
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

        #        *
        #      * *
        #    *   *
        #  * * * * *
        #        *

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==rows-1 or j==rows-1 or i+j==rows:
            res+="."+" "
        else:
            res+=" "+" "
    print(res)

    #  * * * * *
    #  *
    #  * * * * *
    #          *
    #  * * * * *

rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==mid or i==rows or (j==1 and i<=mid) or (j==rows and i>=mid):
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

   
    #  * * * * *
    #  * 
    #  * * * * *
    #  *       *
    #  * * * * *

rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i==mid or j==1 or (j==rows and i>=mid):
            res+="."+" "
        else:
            res+=" "+" "
    print(res)

    # * * * * *
    #       * 
    #     * 
    #   *
    # *

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

    #      * * * 
    #    *       *
    #      * * * 
    #    *       *
    #      * * * 

rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if (i==1 and j!=1 and j!=rows) or (i==mid and j!=1 and j!=rows):
            res+="."+" "
        elif (i==rows and j!=1 and j!=rows) or (j==1 and i!=1 and i!=mid and i!=rows) or (j==rows and i!=1 and i!=mid and i!=rows):
            res+="."+" "
        else:
            res+=" "+" "
    print(res)


    # * * * * *
    # *       *
    # * * * * *
    #         *
    # * * * * *

rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==mid or i==rows or j==rows or (j==1 and i<=mid):
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

#   * * * 
# *       *
# *       *
# *       *
#   * * * 

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
     if (i==1 and j!=1 and j!=rows) or (i==rows and j!=1 and j!=rows) or (j==1 and i!=1 and i!=rows) or (j==rows and i!=1 and i!=rows):
            res+="."+" "
     else:
            res+=" "+" "
    print(res)