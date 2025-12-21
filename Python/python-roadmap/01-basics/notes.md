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
```text
10
```

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

---

## variables.py – Soal 2: Deleting name vs deleting object

### Soal
JANGAN RUN.

```python
x = 100
y = x
del x
print(y)
```

### Prediksi Output
```text
100
```

### Jawaban

**Output:**
```text
100
```

`del x` menghapus nama `x`, bukan object yang ditunjuk

### Urutan Kejadian (Mental Model)

1. Object 100 dibuat, `x` menunjuk ke object 100
2. `y` menunjuk ke object yang sama
3. Nama `x` dihapus
4. Object 100 masih hidup karena masih ditunjuk oleh `y`
5. `print(y)` masih valid

## Kesimpulan
`del` menghapus **nama**, bukan **object**.