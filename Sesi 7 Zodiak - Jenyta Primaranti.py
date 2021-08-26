# Penjelasan Setiap Zodiak
a = "Domba Jantan. Pelopor dan perintis dari horoskop roda, energi Aries membantu kita memulai, berjuang untuk keyakinan kita dan tanpa rasa takut menempatkan diri di luar sana."
b = "Banteng. Penyedia tetap dari keluarga horoskop, energy Taurus membantu kita mencari keamanan, menikmati kesenangan duniawi dan menyelesaikan pekerjaan."
c = "Ayam Jago Kembar. Tanda horoskop yang paling serbaguna dan bersemangat, energi Gemini membantu kami berkomunikasi, berkolaborasi dan mengibarkan bendera aneh kami di tiang penuh."
d = "Kepiting. Pengasuh alami roda horoskop, energi Cancer membantu kita terhubung dengan perasaan kita, menanamkan akar yang dalam dan melengkapi sarang keluarga kita."
e = "Singa. Penguasa drama dan agung klan horoskop, energi Leo membantu kita bersinar, mengekspresikan diri dengan berani dan mengenakan hati kita di lengan baju kita."
f = "Gadis. Master penolong dari horoskop roda, energi Virgo mengajari kita untuk melayani, melakukan pekerjaan yang sempurna dan memprioritaskan kesejahteraan diri kita sendiri, orang yang kita cintai dan planet ini."
g = "Timbangan. Kecantikan yang seimbang dari keluarga horoskop, energi Libra menginspirasi kita untuk mencari kedamaian, harmoni, dan kerja sama dan melakukannya dengan gaya dan keanggunan."
h = "Kalajengking. Tanda horoskop yang paling intens dan terfokus, energi Scorpio membantu kita menyelam lebih dalam, menggabungkan kekuatan super kita dan membentuk ikatan yang dibangun untuk bertahan."
i = "Pemanah. Dunia petualang dari horoskop roda, energi Sagitarius menginspirasi kita untuk bermimpi besar, mengejar yang mustahil, dan mengambil risiko tanpa rasa takut."
j = "Kambing. Perencana utama dari keluarga horoskop, energi Capricorn mengajari kita kekuatan struktur dan tujuan jangka panjang."
k = "Tukang Pengangkat Air. Ilmuwan gila dan kemanusiaan dari roda horoskop, energi Aquarius futuristik membantu kita berinovasi dan bersatu untuk keadilan sosial."
l = "Ikan. Pemimpi dan penyembuh dari keluarga horoskop, energi Pisces membangkitkan kasih sayang, imajinasi, dan kesenian, menyatukan kita sebagai satu."

#Input Tanggal
fom = input("Welcome to Jenyta's program. Please input your Birthday (e.g. 01-06-2002) : ")
lis = fom.split("-")

date = lis[0]
month = lis[1]
year = lis[2]

#Capricorn 22 desember - 21 januari
if (date >= '22' and date <= '31' and month == '12') or (date >= '01' and date <= '22' and month == '01'):
   zodiac_sign = ("Capricorn\n" + j)
#Aquarius 22 januari - 21 febuari
elif (date >= '22' and date <= '29' and month == '01') or (date >= '01' and date <= '22' and month == '02'):
   zodiac_sign = ("Aquarius\n" + k)
#Pisces 22 febuari - 21 maret
elif (date >= "22" and date <= '29' and month == '02') or (date >= '01' and date <= '22' and month == '03'):
   zodiac_sign = ("Pisces\n" + l)
#Aries 22 maret - 21 april
elif (date >= '22' and date <= '31' and month == '03') or (date >= '01' and date <= '22' and month == '04'):
    zodiac_sign = ("Aries\n" + a)
#Taurus 22 april - 21 mei
elif (date >= '22' and date <= '30' and month == '04') or (date >= '01' and date <= '22' and month == '05'):
    zodiac_sign = ("Taurus\n" + b)
#Gemini 22 mei - 21 juni
elif (date >= '22' and date <= '29' and month == '05') or (date >= '01' and date <= '22' and month == '06'):
    zodiac_sign = ("Gemini\n" + c)
#Cancer 22 juni - 21 juli
elif (date >= '22' and date <= '30' and month == '06') or (date >= '01' and date <= '21' and month == '07'):
    zodiac_sign = ("Cancer\n" + d)
#Leo 22 juli - 21 agustus
elif (date >= '22' and date <= '31' and month == '07') or (date >= '01' and date <= '21' and month == '08'):
    zodiac_sign = ("Leo\n" + e)
#Virgo 22 agustus - 21 september
elif (date >= '22' and date <= '31' and month == '08') or (date >= '01' and date <= '21' and month =='09'):
    zodiac_sign = ("Virgo\n" + f)
#Libra 22 september - 21 oktober
elif (date >= '22' and date <= '30' and month == '09') or (date >= '01' and date <= '21' and month == '10'):
    zodiac_sign = ("Libra\n" + g)
#Scorpios 22 oktober - 21 november
elif (date >= '22' and date <= '30' and month == '10') or (date >= '01' and date <= '21' and month == '11'):
    zodiac_sign = ("Scorpio\n" + h)
#Sagitarius 22 november - 21 desember
elif (date >= '22' and date <= '30' and month == '11') or (date >= '01' and date <= '21' and month == '12'):
    zodiac_sign = ("Sagitarius\n" + i)
print("Hello! your zodiac sign is :",zodiac_sign)