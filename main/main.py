#11
words = ["salom", "dunyo", "python", "kod", "salom"]
uzunliklar = {len(w) for w in words}
print(uzunliklar)

#12
juft_toq = {f"{x}-even" if x % 2 == 0 else f"{x}-odd" for x in range(1, 21)}
print(juft_toq)

#13
words = ["olma", "shaftoli", "gilos", "banan"]
oxirgi_harflar = {w[-1] for w in words}
print(oxirgi_harflar)

#14
satrlar = ["salom", "python3", "a1b2", "hello", "2024-yil", "test"]
raqam_borlar = {s for s in satrlar if any(ch.isdigit() for ch in s)}
print(raqam_borlar)

#15
kopaytmasi6 = {
    x for x in range(1, 51)
    if len(str(x)) > 1 and eval("*".join(str(d) for d in x.__str__())) == 6
}
print(kopaytmasi6)
