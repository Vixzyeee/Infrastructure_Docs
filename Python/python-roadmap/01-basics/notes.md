# Answers – 01-basics

---

## variables.py – Soal 1: Rebinding variable

### Soal
JANGAN RUN.

```python
a = 10
b = a
a = a + 5
print(b)
```

### Prediksi Output
(tulis tebakan lu di sini)

### Jawaban

**Output:**
```text
10
```

`b` tidak berubah karena nama `b` tetap menunjuk ke object 10

### Urutan Kejadian (Mental Model)

1. Object 10 dibuat, `a` menunjuk ke object 10
2. `b` menunjuk ke object yang sama
3. Ekspresi `a + 5` membuat object 15
4. Nama `a` di-rebind ke object 15
5. `b` masih menunjuk ke object 10

## Kesimpulan
Assignment di Python mengubah hubungan **nama** → **object**, bukan object-nya.