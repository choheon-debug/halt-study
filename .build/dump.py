import json,sys
B=json.load(open('/tmp/claude-0/halt/book_final.json'))
for s in B:
    if s['n'] not in map(int,sys.argv[1].split(',')): continue
    print(f"## {s['n']} {s['title']}")
    for b in s['blocks']:
        if b['t']=='table': print("T| "+"\nT| ".join(" | ".join(r) for r in b['rows']))
        elif b['t']=='box': print(f"[{b['k']}] {b['x']}")
        elif b['t'] in ('h2','h3'): print(b['x'])
        elif b['t']=='h4': continue
        else: print(b['x'])
