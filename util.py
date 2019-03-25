"""e88"""

# for solutions with 2 non 1 numbers where l is the length x and y are those numbers:
# 	(x-1)(y-1) = l-1
# 	xy = x+y
#
# 	soluiton using only n's and 1's will be lower than solution using only n+1's and 1's
#

import pydash as _
import itertools
import math


def nthprime_list(num, primelist=[2, 3]):
    toadd = primelist[-1]
    while len(primelist) <= num - 1:
        toadd += 2
        devisable = False
        for j in primelist:
            if j > (toadd ** (1.0 / 2.0)):
                break

            if toadd % j == 0:
                devisable = True
                break
        if not devisable:
            primelist.append(toadd)
    return primelist


def prime_under_list(num, primelist=[2, 3]):
    toadd = primelist[-1]
    while primelist[-1] < num:
        toadd += 2
        devisable = False
        for j in primelist:
            if j > (toadd ** (1.0 / 2.0)):
                break

            if toadd % j == 0:
                devisable = True
                break
        if not devisable:
            primelist.append(toadd)
    return primelist


def prime_factors(n):
    leftover = n
    factors = []
    n_root = int(n ** (1.0 / 2.0))
    p_list = prime_under_list(n_root)
    for p in p_list:
        while leftover % p == 0:
            factors.append(p)
            leftover = leftover / p
    if not leftover == 1:
        factors.append(int(leftover))
    return factors


def groups_with_first(newlist, pre=[]):
    if len(newlist) == 0:
        return [pre + []]
    result = []
    # result = result + [pre+[[newlist[0]]]]
    # print newlist[1:],pre+[[newlist[0]]]
    temp = groups_with_first(newlist[1:], pre + [[newlist[0]]])
    result = result + temp
    for i in range(1, len(newlist)):
        temp = groups_with_first(newlist[i:])
        # print "pre", pre, "temp" , temp, "newlist", newlist
        end = []
        for i in newlist[1:i]:
            end.append([i])
        result = result + map(lambda x: pre + [[newlist[0]] + x[0]] + x[1:] + end, temp)
    return result


def groups_to_factors(grouplist):
    result = []
    for group in grouplist:
        temp = [factor_group_to_nums(group)]
        result += temp
    return result


def factor_group_to_nums(factors):
    return map(lambda z: reduce(lambda x, y: x * y, z), factors)


def all_group(newlist):
    return groups_to_factors(groups_with_first(newlist))


def posible_subfactorig(n):
    result = all_group(prime_factors(n))
    map(lambda x: x.sort(), result)
    for list in result:
        if result.count(list) > 1:
            result.remove(list)
    return result


def product_sum_list_for(n):
    lists = posible_subfactorig(n)
    for i in lists:
        total = sum(i)
        while total < n:
            i.append(1)
            total += 1
    return lists


def product_sum_len_for(n):
    lists = posible_subfactorig(n)
    result = []
    for i in lists:
        total = sum(i)
        result.append(len(i) + n - total)
    return result


def min_product_sum_list_num(n):
    result = []
    foundlengths = []
    for i in range(n + 1):
        result.append(0)
    product_sum_number = 4
    while len(foundlengths) < n:
        if product_sum_number % 1 == 0:
            print(product_sum_number, max(foundlengths + [1]), len(foundlengths))
        for length in product_sum_len_for(product_sum_number):
            if foundlengths.count(length) == 0 and len(result) > length:
                foundlengths.append(length)
                result[length] = product_sum_number
            # elif foundlengths.count(len(list))==0:
            # print len(list)
        product_sum_number += 1
    return result


def min_product_sum_list_list(n):
    result = []
    foundlengths = []
    for i in range(n + 1):
        result.append([])
    product_sum_number = 4
    while len(foundlengths) < n:
        if product_sum_number % 1 == 0:
            print(product_sum_number, max(foundlengths + [1]), len(foundlengths))
        for list in product_sum_list_for(product_sum_number):
            if foundlengths.count(len(list)) == 0 and len(result) > len(list):
                foundlengths.append(len(list))
                result[len(list)] = list
            # elif foundlengths.count(len(list))==0:
            # print len(list)
        product_sum_number += 1
    return result


def remove_duplicates_and_add(list):
    for i in list:
        if list.count(i) > 1:
            list.remove(i)
    return sum(list)


def solve_length_for_numbers(list):
    if len(list) == 1:
        return 1
    else:
        calc_prod = reduce(lambda x, y: x * y, list)
        calc_sum = sum(list)
        number_of_ones = calc_prod - calc_sum
        return len(list) + number_of_ones


def add_prefix(seed_list, prefix):
    result = []
    for List in prefix:
        result.append(List + seed_list)
    return result


def recuse_over_factors(factor_list, prefix):
    result = []
    # print 'start',factor_list,prefix
    if factor_list == [] or factor_list == None:
        return prefix
    if len(factor_list) == 1:
        result = result + add_prefix([factor_list[0]], prefix)
        return result
    # first not grouped
    temp = recuse_over_factors(factor_list[1:], [[factor_list[0]]])
    for List1 in temp:
        result += add_prefix(List1, prefix)
    # for frist grouped with second on
    for group_num in range(1, len(factor_list)):
        # do group with group_num
        rest_of_list = factor_list[group_num + 1 :]
        grouped_value = factor_list[0] * factor_list[group_num]
        passed_values = factor_list[1:group_num]
        list_with_group = rest_of_list + [grouped_value]
        # print rest_of_list,grouped_value,passed_values,list_with_group,group_num
        solutions_with_passed_values = recuse_over_factors(passed_values, [[]])
        solutions_with_grouped_values_and_passed_values = recuse_over_factors(
            list_with_group, solutions_with_passed_values
        )
        # print 'big',solutions_with_grouped_values_and_passed_values
        for solution in solutions_with_grouped_values_and_passed_values:
            result += add_prefix(solution, prefix)
    # 	temp1.append(factor_list[0]*factor_list[group_num])
    # 	print 'e',temp1
    # 	temp2 = recuse_over_factors(factor_list[1:group_num],[[]]);
    # 	print 'f',temp2
    # 	result = result + recuse_over_factors(temp1,temp2)
    return result


cache = [1, 2, 3, 5]


def feb(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        cur = len(cache)
        if cur >= n:
            return cache[n - 1]
        else:
            while len(cache) < n:
                cache.append(cache[-1] + cache[-2])
            return cache[n - 1]


def orderings(n_range, n):
    combinations = itertools.combinations(n_range, n)
    permutations = (
        _.chain(combinations)
        .map_(lambda x: itertools.permutations(x))
        .reduce_(lambda x, y: list(x) + list(y))
        .value()
    )
    return permutations


def decimal_from_list(l):
    return _.reduce_(l, lambda x, y: 10 * x + y)
