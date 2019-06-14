# 문제1.
# 다음 세 개의 리스트가 있을 때,
# subs = [‘I’, ‘You’]
# verbs = [‘Play’, ‘Love’]
# objs = [‘Hockey’, ‘Football’]
#
# 3형식 문장을 모두 출력해 보세요. 반드시 comprehension을 사용합니다.


subs = ["I", "You"]
verbs = ["Play", "Love"]
objs = ["Hockey", "Football"]

[print(subs[a], verbs[b], objs[c]) for a in range(0, len(subs)) for b in range(0, len(verbs)) for c in range(0, len(objs))]
