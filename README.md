# Порівняльний аналіз алгоритмів
Було проведено симуляцію видачі решти покупцеві з набору монет номіналом **[50, 25, 10, 5, 2, 1]** та **[10, 6, 1]** з використанням жадібного алгоритму та алгоритму динамічного програмування.
Для заміру часу використовувався модуль [timeit](https://docs.python.org/uk/3/library/timeit.html).\
Алгоритми були запущені по 1000 разів для видачі різних сум решти **113**, **42**, **12**, та **54321**.\
Було отримано наступні данні:

---

Case for **[50, 25, 10, 5, 2, 1]** and sum: **113**\
Result for find_coins_greedy: **{50: 2, 10: 1, 2: 1, 1: 1}**\
Time taken for **find_coins_greedy: 0.000445 seconds**\
Result for find_min_coins: **{50: 2, 10: 1, 2: 1, 1: 1}**\
Time taken for **find_min_coins: 0.041058 seconds**\
\
Case for **[50, 25, 10, 5, 2, 1]** and sum: **42**\
Result for find_coins_greedy: **{25: 1, 10: 1, 5: 1, 2: 1}**\
Time taken for f**ind_coins_greedy: 0.000536 seconds**\
Result for find_min_coins: **{25: 1, 10: 1, 5: 1, 2: 1}**\
Time taken for f**ind_min_coins: 0.014016 seconds**\
\
Case for **[10, 6, 1]** and sum: **12**\
Result for find_coins_greedy: **{10: 1, 1: 2}**\
Time taken for **find_coins_greedy: 0.000313 seconds**\
Result for find_min_coins: **{6: 2}**\
Time taken for **find_min_coins: 0.003088 seconds**\
\
Case for **[50, 25, 10, 5, 2, 1]** and sum: **54321**\
Result for find_coins_greedy: **{50: 1086, 10: 2, 1: 1}**\
Time taken for **find_coins_greedy: 0.000556 seconds**\
Result for find_min_coins: **{50: 1086, 10: 2, 1: 1}**\
Time taken for **find_min_coins: 24.397182 seconds**\

---

На основі отриманих даних видно що жадібний алгоритм виявився швидшим у всіх випадках, а особливо при великих сумах різниця в швидкості сягає кілька порядків. Але ящо треба найоптимальніше рішення і не важлива швидкість виконання, то тоді алгоритм динамічного програмування підходить краще, як видно на прикладі з набіром монет **[10, 6, 1]** та сумою **12** - жадібний алгоритм видає швидке рішення у вигляді монет номіналом **10**, **1** та **1**, а динамічний оптимальне у вигляді монет **6** та **6**.