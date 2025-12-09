# Завдання 1
a=[1, 2, 3, 4, 5]
prefix=[0]*len(a)
prefix[0]=a[0]
for i in range(1, len(a)):
    prefix[i]=prefix[i-1]+a[i]
print(prefix)

# Завдання 2
a = [1, 2, 3, 4, 5]
prefix=[0]*len(a)
prefix[0]=a[0]
for i in range(1, len(a)):
    prefix[i] = prefix[i-1] + a[i]
l, r = 1, 3
if l == 0:
    result = prefix[r]
else:
    result = prefix[r] - prefix[l-1]
print(result)

#3
a=[5, 1, 3, 2, 4]
prefix=[0]*len(a)
prefix[0]=a[0]
for i in range(1, len(a)):
    prefix[i]=prefix[i-1] + a[i]

queries=[(0, 2), (1, 3), (2, 4)]

for l, r in queries:
    if l==0:
        print(prefix[r])
    else:
        print(prefix[r]-prefix[l-1])

#4
a=[2, 1, 5, 1, 3, 2]
k=3
window_sum=sum(a[:k])
max_sum=window_sum
for i in range(k, len(a)):
    window_sum+=a[i]-a[i-k]
    max_sum=max(max_sum, window_sum)
print(max_sum)

#5
a=[3, 4, -2, 1, 6]
S=5
prefix_sum=0
seen={0}
found=False
for x in a:
    prefix_sum+=x
    if prefix_sum - S in seen:
        found=True
        break
    seen.add(prefix_sum)
print("YES" if found else "NO")

