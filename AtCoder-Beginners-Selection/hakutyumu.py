S = input()

def can_form_string(s):
    words = ["dream", "dreamer", "erase", "eraser"]
    
    while s:
        matched = False
        for word in words:
            if s.endswith(word):
                s = s[:-len(word)]
                matched = True
                break
        if not matched:
            return False
    return True

if can_form_string(S):
    print("YES")
else:
    print("NO")