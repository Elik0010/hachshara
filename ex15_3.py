import unittest
import random



def quick_rec(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError
        if len(numbers) == 1 or len(numbers) == 0:
            return numbers
        list_u = []
        list_o = []
        list_b = []
        pivot = random.choice(numbers)
        for i in numbers:
            if i > pivot:
                list_o.append(i)
            elif i < pivot:
                list_u.append(i)
            else:
                list_b.append(i)
        if list_o == [] and list_u == []:
            return list_b
        return quick_rec(list_u + list_b) + quick_rec(list_o)
    except:
        print("error")




class tester(unittest.TestCase):
    def setUp(self):
        self.normal = [4,8,7,6,5,9,2,3,1]
        self.sameish = [1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1]
        self.mixtypes = ['5',3,6,'2',9,1,'6']
        self.allsame = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
        self.tuple = (4,5,8,7,6,9,1,3,2)
        self.empty = []
        self.string = 'fhfhf'
        self.integer = 12345
        self.float = 10.54
        





    def runTest(self):
        self.assertEqual(quick_rec(self.normal), [1,2,3,4,5,6,7,8,9])
        self.assertEqual(quick_rec(self.sameish), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
        self.assertEqual(quick_rec(self.allsame), [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8])
        self.assertEqual(quick_rec(self.empty), [])
        self.assertEqual(quick_rec(self.tuple), [1,2,3,4,5,6,7,8,9])
        self.assertRaises(TypeError, quick_rec(self.string))
        self.assertRaises(TypeError, quick_rec(self.integer))
        self.assertRaises(TypeError, quick_rec(self.float))



if __name__ == '__main__':
    unittest.main()