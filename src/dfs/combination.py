import unittest


def combination(arr, k):
    if len(arr) == 0 or k == 0 or k > len(arr):
        return []

    result = []  # 结果
    record_path = []  # 辅助路径数组
    init_index = 0  # 起始元素下标

    def dfs(source, path, start_index):
        if len(path) == k:
            # 遍历深度到了指定层级
            result.append(path.copy())  # 将此时的路径添加为答案
            return  # 停止递归
        for i in range(start_index, len(source)):
            # 从上一次传下来的下标开始遍历
            path.append(source[i])  # 记录走过的路径
            dfs(source, path, i + 1)  # 将当前元素下标+1作为下次循环的起点，缩小递归的规模
            path.pop()  # 本次循环的递归结束，将当前循环的元素下标从路径中弹出

    dfs(arr, record_path, init_index)  # 执行深度遍历
    return result


class TestCombination(unittest.TestCase):
    def test(self):
        self.assertEqual([], combination(['a', 'b', 'c', 'd'], 0))
        self.assertEqual([['a'], ['b'], ['c'], ['d']], combination(['a', 'b', 'c', 'd'], 1))
        self.assertEqual([
            ['a', 'b'],
            ['a', 'c'],
            ['a', 'd'],
            ['b', 'c'],
            ['b', 'd'],
            ['c', 'd'],
        ], combination(['a', 'b', 'c', 'd'], 2))
        self.assertEqual([
            ['a', 'b', 'c'],
            ['a', 'b', 'd'],
            ['a', 'c', 'd'],
            ['b', 'c', 'd'],
        ], combination(['a', 'b', 'c', 'd'], 3))


def pick_courses(courses, safe_course_pairs, pick_count):
    """" 无冲突选课算法 """

    def transform_to_safe_dict(safe_pairs):
        """" 将无冲突对转为目标 dict """

        def insert_to(d, key, value):
            if key not in d:
                d[key] = [value]
            else:
                d[key].append(value)

        result = {}
        for pair in safe_pairs:
            # 注意 pair 为 'a b' 字符串形式
            c1 = pair[0]
            c2 = pair[2]
            insert_to(result, c1, c2)
            insert_to(result, c2, c1)

        return result

    def is_conflict(pair, safe_relation_dict):
        """判断课程对是否冲突"""
        course_a, course_b = pair
        if course_a not in safe_relation_dict:
            return False
        no_conflict_list = safe_relation_dict[course_a]
        return course_b not in no_conflict_list

    def is_selection_conflict(selection, safe_relation_dict):
        """判断课程组合是否存在冲突"""
        possible_course_pairs = combination(selection, 2)
        for pair in possible_course_pairs:
            if is_conflict(pair, safe_relation_dict):
                return True
        return False

    safe_relation_dict = transform_to_safe_dict(safe_course_pairs)
    result = []
    possible_selection = combination(courses, pick_count)
    for selection in possible_selection:
        if not is_selection_conflict(selection, safe_relation_dict):
            result.append(selection)
    return result


class TestHKUExam(unittest.TestCase):
    def test(self):
        courses = ['a', 'b', 'c', 'd']
        safe_course_pairs = ['a b', 'a c', 'b c']
        self.assertEqual([['a', 'b', 'c']], pick_courses(courses, safe_course_pairs, 3))


def get_courses_from_input():
    count = int(input('please specify the numbers of the following courses: '))
    if not count > 0:
        raise ValueError('numbers of courses should be positive!')
    result = []
    for i in range(count):
        result.append(input('course name: '))
    return result


def get_safe_course_pairs_from_input():
    count = int(input('please specify the numbers of the following safe-course pairs: '))
    if not count > 0:
        raise ValueError('numbers of safe-course pairs should be positive!')
    result = []
    for i in range(count):
        result.append(input('please input a pair of safe courses (separate by blank, e.g. "a b"): '))
    return result


def solution():
    courses = get_courses_from_input()
    safe_course_pairs = get_safe_course_pairs_from_input()
    answers = pick_courses(courses, safe_course_pairs, 3)
    print('You have {0} solutions'.format(len(answers)))
    for answer_courses in answers:
        print('- {0}'.format(' '.join(answer_courses)))


if __name__ == '__main__':
    solution()
