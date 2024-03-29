def parallel_processing(n, m, data):
    output = [(0, i) for i in range(n)]
    result = []
    for ti in data:
        finish_time, output_index = min(output)
        result.append((output_index, finish_time))
        output[output_index] = (finish_time + ti, output_index)
    return result

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for i in range(m):
        print(result[i][0], result[i][1])
        
if __name__ == "__main__":
    main()
