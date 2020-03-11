if len(t) > len(s):
        val = len(s);
        holder = t[:val]
        rem = len(t) -len(holder)


        for idx,emt in enumerate(holder):
            if holder[idx] == s[idx]:
                noise = []
                continue;
            else:
                noise= s[idx:]
                break;

        if 2*len(noise) + rem <= k:
            return "Yes";
        else:
            return "No";

        print("Hello")    
        if len(s) > len(t):
            print("S is larger")
            val = len(t);
            holder = s[:val]
            Enoise = len(s) -len(holder)

            for idx,emt in t:
                if t[idx] == holder[idx]:
                    noise = []
                    continue;
                else:
                    noise = holder[idx:]
                    break;
            if 2*len(noise)+Enoise <= k:
                return "Yes";
            else:
                return "No";    

    if len(s) == len(t):
        for idx,emt in t:
            if t[idx] == s[idx]:
                noise = [];
                continue
            else:
                noise = s[idx:]
                break;
        
        if 2*len(noise)<= k:
            return "Yes"
        else:
            return "No"  