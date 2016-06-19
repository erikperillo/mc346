def brancos(file_name):
    try:
        f = open(file_name)
        try:
            return "".join(f).count(" ")
        except:
            return "falha ao ler"
        finally:
            f.close()
    except:
        return "falha ao abrir"
