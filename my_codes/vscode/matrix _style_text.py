import time
main_string = input("Enter Input String:  ").lower()
cryptic_string = '''à á â ä ã å ā ă ą ȧ ç ć č ĉ ċ ð ď đ è é ê ë ē ė ę ĕ ě ĝ ğ ġ ģ ĥ ħ ì í î ï ĩ ī į ı ĵ ķ ĺ ļ ľ ŀ ł ñ ń ņ ň ŋ ò ó ô ö õ ō ŏ ǒ ø ǫ ŕ ŗ ř ś ŝ š ş ţ ť ŧ ù ú û ü ũ ū ŭ ů ų ű ŵ ý ŷ ÿ ź ż ž æ Æ œ Œ ß ƒ þ Þ Ð ð Ȝ ƿ Ɛ ȝ ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ ] ^ _ ` { | } ~ ± × ÷ ∑ ∞ ≠ ≤ ≥ ≈ ∫ √ ∆ ∂ ∏ ∝ £ € ¥ ¢ ₹ ₩ ₽ ₱ © ® ™ § ¶ † ‡ ° ¬ • ‼ ‽ ⁂ ⁑ ⁇ ‾ ‵ ‷ ¯ ← ↑ → ↓ ↔ ↕ ↖ ↗ ↘ ↙ ▲ ▼ ◀ ▶ ◆ ■ ▪ ● 𝒶 𝒷 𝒸 𝒹 𝒺 𝒻 𝒼 𝒽 𝒾 𝒿 𝓀 𝓁 𝓂 𝓃 𝓄 𝓅 𝓆 𝓇 𝓈 𝓉 𝓊 𝓋 𝓌 𝓍 𝓎 𝓏 𝔞 𝔟 𝔠 𝔡 𝔢 𝔣 𝔤 𝔥 𝔦 𝔧 𝔨 𝔩 𝔪 𝔫 𝔬 𝔭 𝔮 𝔯 𝔰 𝔱 𝔲 𝔳 𝔴 𝔵 𝔶 𝔷 𝕒 𝕓 𝕔 𝕕 𝕖 𝕗 𝕘 𝕙 𝕚 𝕛 𝕜 𝕝 𝕞 𝕟 𝕠 𝕡 𝕢 𝕣 𝕤 𝕥 𝕦 𝕧 𝕨 𝕩 𝕪 𝕫 ᴀ ʙ ᴄ ᴅ ᴇ ᴇ ᴇ ᴘ ᴘ ᴘ ᵃ ᵇ ᶜ ᶻ ₐ ₑ ₒ ₓ
abcdefghijklmnopqrstuvwxyz'''
output_string = ''
for i in main_string:
    if i == ' ':
        output_string += ' '
        print
        print(output_string)
        continue
    for j in cryptic_string:
        time.sleep(0.0001)
        if i==j:
            output_string += i
            print(output_string)
            break
        
        print(output_string+j)
print()
print(output_string)