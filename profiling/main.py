import io
import pstats

from bin_tree_non_recursive import gen_bin_tree_non_recursive
from bin_tree_recursive import gen_bin_tree_recursive

"""
@:param - n - количество итераций
"""
def setup_data(n: int) -> list:
    from random import randint
    min_height = 17
    max_height = 17
    min_root = 50
    max_root = 100
    data = [None] * n
    for i in range(n):
        height = randint(min_height, max_height)
        root = randint(min_root, max_root)
        data[i] = (height, root)
    return data


"""
Расчет времени TimeIt:
- оценка зависимости времени расчетов от количества итераций расчетов
@:param - n - количетсво итераций
"""
def calculate_time_timeit(n: int, func) -> float:
    import timeit
    data = setup_data(n)
    delta = 0
    for i, height_root_tuple in enumerate(data):
        start_time = timeit.default_timer()
        func(*height_root_tuple)
        delta += timeit.default_timer() - start_time
        # print(f"[{i}] height: {height_root_tuple[0]} root: {height_root_tuple[1]} delta: {delta}")
    return delta

"""
Расчет времени cProfile:
- оценка зависимости времени расчетов от количества итераций расчетов
@:param - n - количетсво итераций
"""
def calculate_time_cprofile(n: int, func):
    import cProfile
    pr = cProfile.Profile()
    data = setup_data(n)
    pr.enable()
    for i, height_root_tuple in enumerate(data):
        func(*height_root_tuple)
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    return s.getvalue()


def handle_cProfile_results(result_events: list):
    execution_times = [None]
    for event_text in result_events:
        for line in event_text.splitlines():
            if 'bin_tree_recursive' in line or 'bin_tree_non_recursive' in line:
                parts = line.split()
                execution_time = parts[3]
                execution_times.append(float(execution_time))
                break
    return execution_times


def main():
    # TimeIt
    import matplotlib.pyplot as plt
    res_rec = [None]
    for n in range(1, 11):
        res_rec.append(calculate_time_timeit(n, gen_bin_tree_recursive))
    res_non_rec = [None]
    for n in range(1, 11):
        res_non_rec.append(calculate_time_timeit(n, gen_bin_tree_non_recursive))

    # cProfile
    res_rec_cprof = []
    for n in range(1, 11):
        res_rec_cprof.append(calculate_time_cprofile(n, gen_bin_tree_recursive))
    res_non_rec_cprof = []
    for n in range(1, 11):
        res_non_rec_cprof.append(calculate_time_cprofile(n, gen_bin_tree_non_recursive))

    exec_times_rec = handle_cProfile_results(res_rec_cprof)
    exec_times_non_rec = handle_cProfile_results(res_non_rec_cprof)


    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(res_rec, label='Рекурсивно')
    plt.plot(res_non_rec, label='Нерекурсивно')
    plt.legend()
    plt.xlabel('Количество бинарных деревьев на одну итерацию')
    plt.ylabel('Время построения')
    plt.xticks(ticks=range(1, 11, 1))
    plt.title('Время рекурсивного и нерекурсивного построения бинарных деревьев высотой H=17\nTimeIt')

    plt.subplot(1, 2, 2)
    plt.plot(exec_times_rec, label='Рекурсивно')
    plt.plot(exec_times_non_rec, label='Нерекурсивно')
    plt.legend()
    plt.xlabel('Количество бинарных деревьев на одну итерацию')
    plt.ylabel('Время построения')
    plt.xticks(ticks=range(1, 11, 1))
    plt.title('Время рекурсивного и нерекурсивного построения бинарных деревьев высотой H=17\ncProfile')


    plt.show()

if __name__ == "__main__":
    main()
