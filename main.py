def parallel_processing(n, m, data):
    output = [(0, i) for i in range(n)]
    result = []
    for i in range(m):
        ti = data[i]
        finish_time, output_index = output[0]
        result.append((output_index, finish_time))
        output[0] = (finish_time + ti, output_index)
        j = 0
        while j < n-1 and output[j][0] > output[j+1][0]:
            output[j], output[j+1] = output[j+1], output[j]
            j += 1
    return result

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for i in range(m):
        print(result[i][0], result[i][1])

if __name__ == "__main__":
    main()
