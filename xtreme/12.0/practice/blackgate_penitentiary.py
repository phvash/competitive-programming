crew_members = {120: [], 121: [], 122: [], 123: [], 124: [], 125: [], 126: [], 127: [], 128: [], 129: [], 130: [], 131: [], 132: [], 133: [], 134: [], 135: [], 136: [], 137: [], 138: [], 139: [], 140: [], 141: [], 142: [], 143: [], 144: [], 145: [], 146: [], 147: [], 148: [], 149: [], 150: [], 151: [], 152: [], 153: [], 154: [], 155: [], 156: [], 157: [], 158: [], 159: [], 160: [], 161: [], 162: [], 163: [], 164:[], 165: [], 166: [], 167: [], 168: [], 169: [], 170: [], 171: [], 172: [], 173: [], 174: [], 175: [], 176: [], 177: [], 178: [], 179: [], 180: [], 181: [], 182: [], 183: [], 184: [], 185: [], 186: [], 187: [], 188: [], 189: [], 190: [], 191: [], 192: [], 193: [], 194: [], 195: [], 196: [], 197: [], 198: [], 199: [], 200: [], 201: [], 202: [], 203: [], 204: [], 205: [], 206: [], 207: [], 208: [], 209: [], 210: [], 211: [], 212: [], 213: [], 214: [], 215: [], 216: [], 217: [], 218: [], 219: [], 220: [], 221: [], 222: [], 223: [], 224: [], 225: [], 226: [], 227: [], 228: [], 229: [], 230: [], 231: [], 232: [], 233: [], 234: [], 235: [], 236: [], 237: [], 238: [],239: [], 240: [], 241: [], 242: [], 243: [], 244: [], 245: [], 246: [], 247: [], 248: [], 249: [], 250: []}
    
n = int(input())

for i in range(n):
    name, height = input().strip(' ').split(' ')
    height = int(height)
    crew_members_with_height = crew_members[height]
    crew_members_with_height.append(name)
    crew_members[height] = crew_members_with_height

total_count = 0
for _height in crew_members:
    _members = crew_members[_height]
    if _members:
        start_index = total_count + 1
        end_index = total_count + len(_members)
        print(' '.join(sorted(_members)), start_index, end_index)
        total_count = end_index




