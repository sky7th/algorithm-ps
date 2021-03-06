#타겟 넘버
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
def DFS(numbers, target, index, num):
    if index == len(numbers):
        return 1 if num == target else 0
    else:
        return DFS(numbers, target, index+1, num + numbers[index]) \
                + DFS(numbers, target, index+1, num - numbers[index])
    return

def solution(numbers, target):
    return DFS(numbers, target, 0, 0)
#좋은 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


#네트워크
#좋은 풀이
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    print(visited)
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer


#단어 변환
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
from collections import deque as queue

transistable = lambda a,b: sum((1 if x!=y else 0) for x,y in zip(a,b)) == 1

def solution(begin, target, words):
    q, d = queue(), dict()
    q.append((begin, 0))
    d[begin] = set(filter(lambda x:transistable(x,begin), words))

    for w in words:
        d[w] = set(filter(lambda x:transistable(x,w), words))

    while q:
        cur, level = q.popleft()
        if level > len(words):
            return 0
        for w in d[cur]:
            if w == target:
                return level+1
            else:
                q.append((w, level+1))

    return 0


#여행 경로
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.
from collections import defaultdict 

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()
    print(graph, 'a')

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer

