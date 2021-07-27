import os


def new_struct_info():
    pliki = [f"macierz_struktury_nowa/{i}" for i in os.listdir("macierz_struktury_nowa")]
    wyniki = {}
    for nazwa_pl in pliki:
        plik_h = open(nazwa_pl)
        plik = plik_h.readlines()[1:]
        plik_h.close()
        for i in plik:
            data = i.split(",")
            seq_name = data[0]
            if len(seq_name.split(" ")) > 1:
                seq_name = seq_name.split(" ")[0]
            features = []
            for i1 in data:
                try:
                    features.append(int(i1))
                except ValueError:
                    continue
            if not features:
                features = ["?" for i in range(int((len(data)-1)/2))]
            if seq_name in wyniki:
                wyniki[seq_name].extend(features)
            else:
                wyniki[seq_name] = features
    return wyniki


if __name__ == "__main__":
    new_struct_info()
