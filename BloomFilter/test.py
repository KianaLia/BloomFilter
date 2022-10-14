from simplebloomfilter import SimpleBloomFilter
from advancedbloomfilter import AdvancedBloomFilter

if __name__ == '__main__':
    print('Testing SimpleBloomFilter: \n')
    x = SimpleBloomFilter(20,2)
    x.properties()
    x.insert(2)
    x.insert(-10)
    x.insert(12)
    x.insert(31)
    x.insert(987)
    x.show()

    # test_cases = [30, 2, -1, 987]
    test_cases = [12]
    for test in test_cases:
        print(f'is {test} in Set? {x.lookup(test)}')

    print('Testing AdvancedBloomFilter: \n')
    x = AdvancedBloomFilter(5,0.01)
    x.properties()
    x.insert(2)
    x.insert(-10)
    x.insert(12)
    x.insert(31)
    x.insert(987)
    x.show()

    for test in test_cases:
        print(f'is {test} in Set? {x.lookup(test)}')