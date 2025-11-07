import numpy as np

x = list(np.random.randint(low=1, high=20,size=30))

def constante(x:list) -> list:
    return x

print(constante(x))


'''def ordenar_desc(arr, n):
    for i in range(1, n):
        pos_act = i
        elemm_act = arr[i]
        while pos_act > 0 and arr[pos_act -1] < arr[pos_act]:
            arr[pos_act] = arr[pos_act - 1]
            pos_act -= 1
            arr[pos_act] = elemm_act
    return arr

if __name__ == "__main__":
    arr = [4, 6, 2, 5]
    ordenar(arr, 4)
    print("El arreglo ordenado es: ", arr)'''



def ordenar_asc(arr, n):
    for i in range(1, n):
        pos_act = i
        elemm_act = arr[i]
        while pos_act > 0 and arr[pos_act] < arr[pos_act - 1]:
            arr[pos_act] = arr[pos_act - 1]
            pos_act -= 1
            arr[pos_act] = elemm_act
    return arr

if __name__ == "__main__":
    arr = [4, 6, 2, 5]
    ordenar_asc(arr, 4)
    print("El arreglo ordenado es: ", arr)