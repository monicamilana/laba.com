from Bio import SeqIO
# Файл GenBank
#
input_file = r"C:/Users/USER/питон задания лаб/sequence.gb"


# Читаем все записи из файла
records = list(SeqIO.parse(input_file, "genbank"))

# Вычисляем GC-состав для каждой последовательности
def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) if len(seq) > 0 else 0

# Создаем список с GC-составом
gc_sorted_records = sorted(records, key=lambda r: gc_content(r.seq))

# Выводим последовательности в порядке возрастания GC-состава
for record in gc_sorted_records:
    gc_value = gc_content(record.seq)
    print(f"{record.id}: {record.description}, GC = {gc_value:.6f}")

###############################################трансляции 

from Bio import SeqIO

# Файл GenBank
#именно в следующей строчке у тебя должен быть путь к твоему файлу который ты делаешь на сайте, ну и наверное название у тебя будет другое
input_file = r"C:/Users/USER/питон задания лаб/sequence.gb"

# Читаем все записи
records = list(SeqIO.parse(input_file, "genbank"))

# Обрабатываем кодирующие последовательности
for record in records:
    for feature in record.features:# Каждый feature — это аннотированный фрагмент последовательности, содержащий информацию о гене, кодирующем участке
        if feature.type == "CDS": #Проверяем, является ли данный feature кодирующей последовательностью (CDS — Coding DNA Sequence, то есть участок ДНК, который кодирует белок)
            start = feature.location.start  # Получаем координаты начала (start) и конца (end) кодирующего участка на последовательности. feature.location.start и .end содержат числовые позиции участка.
            end = feature.location.end  # Убираем .position
            strand = feature.location.strand#Определяем направление цепи (1 — прямая цепь, -1 — комплементарная).
            
            protein_sequence = feature.qualifiers.get("translation", ["Нет данных"])[0]#Извлекаем аминокислотную последовательность белка, если она доступна в аннотациях (qualifiers). Если перевода нет, возвращается "Нет данных"
            
            print(f"{record.id}: {record.description}")#Выводим идентификатор (id) и описание (description) последовательности.
            print(f"Coding sequence location = [{start}:{end}] ({'+' if strand == 1 else '-'})")#Выводим местоположение кодирующего участка (start:end) и его направление (+ для 1, - для -1).
            print(f"Translation =\n{protein_sequence}\n")#Печатаем аминокислотную последовательность белка.
