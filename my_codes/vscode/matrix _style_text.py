import time
main_string = input("Enter Input String:  ").lower()
cryptic_string = "àáâäãåāăąȧçćčĉċðďđèéêëēėęĕěĝğġģĥħìíîïĩīįıĵķĺļľŀłñńņňŋòóôöõōŏǒøǫŕŗřśŝšşťŧùúûüzūŭůųűŵýŷÿźżžæÆœŒßƒþÞÐðȜƿƐȝ!\"#$%'()*+,-./:;<=>?@[]^_`{|}~±×÷∑∞≠≤≥≈∫√∆∂∏£€¥₹₩₽₱©®™§¶†‡¬•‼‽⁂⁑⁇‾‵‷¯←↑→↓↔↕↖↗↘↙▲▼◀▶◆■▪●𝒶𝒷𝒸𝒹𝒺𝒻𝒼𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝓄𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓏𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫ᴀʙᴄᴅᴇᴇᴇᴘᴘᴘᵃᵇᶜᶻₐₑₒₓabcdefghijklmnopqrstuvwxyz"
output_string = ''
for i in main_string:
    if i == ' ':
        output_string += ' '
        # print
        print(output_string)
        continue
    for j in cryptic_string:
        time.sleep(0.000001)
        if j==' ':
            continue
        elif i==j:
            output_string += i
            print(output_string)
            break
        
        print(output_string+j)
print()
for _ in range(50):
    time.sleep(0.00000001)
    print(output_string)