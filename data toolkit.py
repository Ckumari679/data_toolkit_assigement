{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e6e9eb78-e4cc-4636-a9df-ab9da31da7a9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "b60f9983-b885-440e-a429-5f9cce1622c7",
   "metadata": {},
   "source": [
    "DATA TOOLKIT "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b8f40f27-ee7f-4046-baca-ebd2f8f6fcc8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d4b256c3-4639-476a-b073-cb638aa1808d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Demonstrate three different methods for creating identical 2D arrays in NumPy Provide the code for each\n",
    "#method and the final output after each method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "53ade750-7d9b-4e3b-9cd5-d5fd397d2407",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3d40b8ce-6108-4e18-a7ad-bf22093074e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 3, 3],\n",
       "       [3, 3, 3]])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1=np.array([[3,3,3],[3,3,3]])\n",
    "arr1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9277ee08-da29-4027-8be3-43550d48fe58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 3, 3],\n",
       "       [3, 3, 3]])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr=np.array([3,3,3,3,3,3])\n",
    "arr2=arr.reshape((2,3))\n",
    "arr2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b7680869-903e-4e4d-936c-010aee171de3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 3, 3],\n",
       "       [3, 3, 3]])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar = np.ones((2,3),dtype=int)\n",
    "arr3 = ar+2\n",
    "arr3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ed4751a-e449-4ce6-9970-e00bb33b9daa",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "37fd604d-bf5a-45ff-b453-f2d841194523",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "604d8efe-5c5e-440b-a49d-e8628f620c07",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Using the Numpy function, generate an array of 100 evenly spaced numPers Petween 1 and 10 and\n",
    "#Reshape that 1D array into a 2D array\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0ac300ac-c4c3-4050-98f8-31df4389142a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1.        ,  1.09090909,  1.18181818,  1.27272727,  1.36363636,\n",
       "        1.45454545,  1.54545455,  1.63636364,  1.72727273,  1.81818182,\n",
       "        1.90909091,  2.        ,  2.09090909,  2.18181818,  2.27272727,\n",
       "        2.36363636,  2.45454545,  2.54545455,  2.63636364,  2.72727273,\n",
       "        2.81818182,  2.90909091,  3.        ,  3.09090909,  3.18181818,\n",
       "        3.27272727,  3.36363636,  3.45454545,  3.54545455,  3.63636364,\n",
       "        3.72727273,  3.81818182,  3.90909091,  4.        ,  4.09090909,\n",
       "        4.18181818,  4.27272727,  4.36363636,  4.45454545,  4.54545455,\n",
       "        4.63636364,  4.72727273,  4.81818182,  4.90909091,  5.        ,\n",
       "        5.09090909,  5.18181818,  5.27272727,  5.36363636,  5.45454545,\n",
       "        5.54545455,  5.63636364,  5.72727273,  5.81818182,  5.90909091,\n",
       "        6.        ,  6.09090909,  6.18181818,  6.27272727,  6.36363636,\n",
       "        6.45454545,  6.54545455,  6.63636364,  6.72727273,  6.81818182,\n",
       "        6.90909091,  7.        ,  7.09090909,  7.18181818,  7.27272727,\n",
       "        7.36363636,  7.45454545,  7.54545455,  7.63636364,  7.72727273,\n",
       "        7.81818182,  7.90909091,  8.        ,  8.09090909,  8.18181818,\n",
       "        8.27272727,  8.36363636,  8.45454545,  8.54545455,  8.63636364,\n",
       "        8.72727273,  8.81818182,  8.90909091,  9.        ,  9.09090909,\n",
       "        9.18181818,  9.27272727,  9.36363636,  9.45454545,  9.54545455,\n",
       "        9.63636364,  9.72727273,  9.81818182,  9.90909091, 10.        ])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array_1=np.linspace(1,10,(100))\n",
    "array_1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "8b954812-7ae5-4e16-9299-71ff3511a2c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.        ,  1.09090909,  1.18181818,  1.27272727,  1.36363636,\n",
       "         1.45454545,  1.54545455,  1.63636364,  1.72727273,  1.81818182],\n",
       "       [ 1.90909091,  2.        ,  2.09090909,  2.18181818,  2.27272727,\n",
       "         2.36363636,  2.45454545,  2.54545455,  2.63636364,  2.72727273],\n",
       "       [ 2.81818182,  2.90909091,  3.        ,  3.09090909,  3.18181818,\n",
       "         3.27272727,  3.36363636,  3.45454545,  3.54545455,  3.63636364],\n",
       "       [ 3.72727273,  3.81818182,  3.90909091,  4.        ,  4.09090909,\n",
       "         4.18181818,  4.27272727,  4.36363636,  4.45454545,  4.54545455],\n",
       "       [ 4.63636364,  4.72727273,  4.81818182,  4.90909091,  5.        ,\n",
       "         5.09090909,  5.18181818,  5.27272727,  5.36363636,  5.45454545],\n",
       "       [ 5.54545455,  5.63636364,  5.72727273,  5.81818182,  5.90909091,\n",
       "         6.        ,  6.09090909,  6.18181818,  6.27272727,  6.36363636],\n",
       "       [ 6.45454545,  6.54545455,  6.63636364,  6.72727273,  6.81818182,\n",
       "         6.90909091,  7.        ,  7.09090909,  7.18181818,  7.27272727],\n",
       "       [ 7.36363636,  7.45454545,  7.54545455,  7.63636364,  7.72727273,\n",
       "         7.81818182,  7.90909091,  8.        ,  8.09090909,  8.18181818],\n",
       "       [ 8.27272727,  8.36363636,  8.45454545,  8.54545455,  8.63636364,\n",
       "         8.72727273,  8.81818182,  8.90909091,  9.        ,  9.09090909],\n",
       "       [ 9.18181818,  9.27272727,  9.36363636,  9.45454545,  9.54545455,\n",
       "         9.63636364,  9.72727273,  9.81818182,  9.90909091, 10.        ]])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array_2=array_1.reshape((10,10))\n",
    "array_2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4513e71b-6bce-4ab6-86d6-5291f4a19689",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ef63caf1-dc64-49b9-a010-ad2353b33071",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f9ca4f1d-b20d-49cf-be6e-87b7fb1eb5f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1.  The difference in np.array, np.asarray and np.asanyarray\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c626f0be-f6a2-4325-9e39-98d6c595bf78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''np.array is use for create a new array'''\n",
    "\n",
    "np.array([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "06989af3-0502-423f-9273-960ee00d4959",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''np.asarray is use to convert any input to an numpy array'''\n",
    "\n",
    "l=[1,2,3,4]\n",
    "np.asarray(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8558f9b8-ad8c-49a8-9714-389a50c2ffb0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 3, 4])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''np.asany array is also used to create a numpy nd array but also create a sub classes'''\n",
    "\n",
    "a=[2,3,4]\n",
    "np.asanyarray(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "841d8b37-fba4-41ef-9a5e-74ea209853cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1f4f6195-2688-4826-a0e5-e8fa562aa16a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2 The difference between Deep copy and shallow copy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "fe947268-35b6-45a2-a9ad-8bfed400bda2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " #shallow copy\n",
    "    \n",
    "#taking a list and convert intu array\n",
    "l=[1,2,3,4,5]\n",
    "arr=np.array(l)\n",
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "26cfb3c4-1c78-443d-8c80-14c3db7854d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#taking a another varible 'x' and putting 'arr'into it\n",
    "x=arr\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "2dfa4556-9c9f-4329-b913-3435ff27718e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1, 200,   3,   4,   5])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#now i change any index value of arr\n",
    "arr[1]=200\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "fc96ed72-698e-4005-978f-527f69527e76",
   "metadata": {},
   "outputs": [],
   "source": [
    "#i am changing the value of 'arr' but 'x' was automatic change this is called shallow copy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6ab9d5e-a563-4652-82f8-12d1ed4aac74",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3d33c5f8-5484-4e59-9ac8-ad606378e03a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1, 200,   3,   4,   5])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#deep copy\n",
    "\n",
    "#we take an another varible'y' and insert a copy of arr\n",
    "y=arr.copy()\n",
    "y\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "35a3bf5e-951f-4f74-85ee-6973c0508951",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1, 500,   3,   4,   5])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#now i am changing any index value of arr\n",
    "arr[1]=500\n",
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "0f699bc9-0c5a-4f24-82c3-f64a39a98366",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1, 200,   3,   4,   5])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "cc67fd12-257d-42bb-bf6b-362d8e9e8c2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#hear we can see that arr has chang index value but y remains as it is ,this is called deep copy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ac9864f-1056-4d31-91c0-4bcf40b04455",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ebb624b4-89a4-4a4b-983a-aa6f5ebb1d83",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "df5391ce-3812-4d05-9670-2a6db5d4cd43",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a 3x3 array with random floating-point numBers Between 5 and 20 Then, round each numBer in\n",
    "#the array to 2 decimal places\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "a09b67aa-288c-4b3c-bd7d-6e207c252676",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[11.08938547, 18.83732208, 19.58268572],\n",
       "       [18.71005192,  6.02830941, 19.84934797],\n",
       "       [ 9.27977306,  6.07259667, 20.85430429]])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array_random=np.random.uniform(5,21,(3,3))\n",
    "array_random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c3cb4c3c-2724-4446-aca0-cd2e97245f10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[11.09, 18.84, 19.58],\n",
       "       [18.71,  6.03, 19.85],\n",
       "       [ 9.28,  6.07, 20.85]])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array_random=np.round(array_random,2)\n",
    "array_random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8735bab7-1c39-496e-9b84-b303d2726553",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b8b4c74a-45e2-43df-bd9f-c22387d78f52",
   "metadata": {},
   "outputs": [],
   "source": [
    "#question 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "95273af5-2d83-4af4-9a33-638e5a14d737",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a NumPy array with random integers Petween 1 and 10 of shape (5, 6)) After creating the array\n",
    "#perform the following operations:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "c8b40641-7faf-4c5a-a25d-f18cf88e8f5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 3,  5,  4,  7,  7,  1],\n",
       "       [ 6,  4,  7,  9, 10,  8],\n",
       "       [ 3, 10,  3,  1, 10,  8],\n",
       "       [ 3,  3,  8,  5,  5,  9],\n",
       "       [ 9,  3,  4, 10,  7,  3]])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "random_array=np.random.randint(1,11,(5,6))\n",
    "random_array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "3c8ffd52-eb95-4f4c-86b6-e45a8e6d66a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 4,  6,  4, 10,  8, 10, 10,  8,  8,  4, 10])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# all even integer\n",
    "\n",
    "even= random_array[random_array%2==0]\n",
    "even"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "1db3513e-7af3-47d6-82f3-2473a33c2146",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 5, 7, 7, 1, 7, 9, 3, 3, 1, 3, 3, 5, 5, 9, 9, 3, 7, 3])"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#all odd integer\n",
    "\n",
    "odd=random_array[random_array % 2!=0]\n",
    "odd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4ed06c5-6538-4cab-9932-5593db759929",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1c6244de-87d0-472e-84a1-788ce2f06b67",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a771ddb4-d8a2-44a5-82ea-39e22ce0b415",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a 3D NumPy array of shape (3, 3,3) containing random integers Petween 1 and 10 Perform the following operations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "72a5ffc1-2fba-4bff-a7c0-294c1cc31e77",
   "metadata": {},
   "outputs": [],
   "source": [
    "array1=np.random.randint(1,11,(3,3,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "89f2bb75-254a-4337-b70b-09f9faf8b22f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ 8,  9, 10],\n",
       "        [ 9,  4,  9],\n",
       "        [ 9,  1,  2]],\n",
       "\n",
       "       [[ 2,  7,  3],\n",
       "        [ 6,  7,  5],\n",
       "        [10, 10,  7]],\n",
       "\n",
       "       [[ 5,  7,  2],\n",
       "        [ 2,  6,  5],\n",
       "        [ 3,  8,  8]]])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "6e1ec715-77d3-41bf-ac18-2699b626ec6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2, 0, 0],\n",
       "       [1, 1, 0],\n",
       "       [1, 1, 1]])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1  maximum indices \n",
    "\n",
    "max_value=np.argmax(array1,axis=2)\n",
    "max_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff51fe9c-a151-49e5-8b59-5955ea8b50a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2  Perform element wise multiplication of between both array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "2e41df7f-ab8d-40eb-b4b9-c5065a6298c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[16,  0,  0],\n",
       "        [ 9,  4,  0],\n",
       "        [ 9,  1,  2]],\n",
       "\n",
       "       [[ 4,  0,  0],\n",
       "        [ 6,  7,  0],\n",
       "        [10, 10,  7]],\n",
       "\n",
       "       [[10,  0,  0],\n",
       "        [ 2,  6,  0],\n",
       "        [ 3,  8,  8]]])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multiplication=np.multiply(array1,max_value)\n",
    "\n",
    "#multiplication=array1*max_value\n",
    "\n",
    "multiplication"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fbf3a9d1-9829-42df-9b41-2e26e60f5724",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d5d2d57a-de47-4e4a-bd6f-03f2c8edf25b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#question 7\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7837c375-86ea-4c05-9579-0527f6ceb58f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Clean and transform the 'Phone' column in the sample dataset to remove non-numeric characters and\n",
    "#convert it to a numeric data type Also display the taPle attriPutes and data types of each column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "6630583c-d505-4e8e-aa30-2235fb665eb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "86180bcc-ac8d-4b11-8190-5ec38a57e333",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Perform the following tasK using people dataset:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "2df34271-d164-4eee-9883-b83ba2cf99ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "#a) Read the 'dataYcsv' file using pandas, skipping the first 50 rows.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4a932496-b263-47ec-bb2e-5bb9d3b330ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "fc3958d7-ee39-4649-8f87-d8c9333a4a98",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('People Data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "0fda8a50-1adf-4461-bfcd-f3dd7c05a103",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Index</th>\n",
       "      <th>User Id</th>\n",
       "      <th>First Name</th>\n",
       "      <th>Last Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Email</th>\n",
       "      <th>Phone</th>\n",
       "      <th>Date of birth</th>\n",
       "      <th>Job Title</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>8717bbf45cCDbEe</td>\n",
       "      <td>Shelia</td>\n",
       "      <td>Mahoney</td>\n",
       "      <td>Male</td>\n",
       "      <td>pwarner@example.org</td>\n",
       "      <td>857.139.8239</td>\n",
       "      <td>27-01-2014</td>\n",
       "      <td>Probation officer</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>3d5AD30A4cD38ed</td>\n",
       "      <td>Jo</td>\n",
       "      <td>Rivers</td>\n",
       "      <td>Female</td>\n",
       "      <td>fergusonkatherine@example.net</td>\n",
       "      <td>NaN</td>\n",
       "      <td>26-07-1931</td>\n",
       "      <td>Dancer</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>810Ce0F276Badec</td>\n",
       "      <td>Sheryl</td>\n",
       "      <td>Lowery</td>\n",
       "      <td>Female</td>\n",
       "      <td>fhoward@example.org</td>\n",
       "      <td>(599)782-0605</td>\n",
       "      <td>25-11-2013</td>\n",
       "      <td>Copy</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>BF2a889C00f0cE1</td>\n",
       "      <td>Whitney</td>\n",
       "      <td>Hooper</td>\n",
       "      <td>Male</td>\n",
       "      <td>zjohnston@example.com</td>\n",
       "      <td>NaN</td>\n",
       "      <td>17-11-2012</td>\n",
       "      <td>Counselling psychologist</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>9afFEafAe1CBBB9</td>\n",
       "      <td>Lindsey</td>\n",
       "      <td>Rice</td>\n",
       "      <td>Female</td>\n",
       "      <td>elin@example.net</td>\n",
       "      <td>(390)417-1635x3010</td>\n",
       "      <td>15-04-1923</td>\n",
       "      <td>Biomedical engineer</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>996</td>\n",
       "      <td>fedF4c7Fd9e7cFa</td>\n",
       "      <td>Kurt</td>\n",
       "      <td>Bryant</td>\n",
       "      <td>Female</td>\n",
       "      <td>lyonsdaisy@example.net</td>\n",
       "      <td>021.775.2933</td>\n",
       "      <td>05-01-1959</td>\n",
       "      <td>Personnel officer</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>997</td>\n",
       "      <td>ECddaFEDdEc4FAB</td>\n",
       "      <td>Donna</td>\n",
       "      <td>Barry</td>\n",
       "      <td>Female</td>\n",
       "      <td>dariusbryan@example.com</td>\n",
       "      <td>001-149-710-7799x721</td>\n",
       "      <td>06-10-2001</td>\n",
       "      <td>Education administrator</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>998</td>\n",
       "      <td>2adde51d8B8979E</td>\n",
       "      <td>Cathy</td>\n",
       "      <td>Mckinney</td>\n",
       "      <td>Female</td>\n",
       "      <td>georgechan@example.org</td>\n",
       "      <td>+1-750-774-4128x33265</td>\n",
       "      <td>13-05-1918</td>\n",
       "      <td>Commercial/residential surveyor</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>999</td>\n",
       "      <td>Fb2FE369D1E171A</td>\n",
       "      <td>Jermaine</td>\n",
       "      <td>Phelps</td>\n",
       "      <td>Male</td>\n",
       "      <td>wanda04@example.net</td>\n",
       "      <td>(915)292-2254</td>\n",
       "      <td>31-08-1971</td>\n",
       "      <td>Ambulance person</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>1000</td>\n",
       "      <td>8b756f6231DDC6e</td>\n",
       "      <td>Lee</td>\n",
       "      <td>Tran</td>\n",
       "      <td>Female</td>\n",
       "      <td>deannablack@example.org</td>\n",
       "      <td>079.752.5424x67259</td>\n",
       "      <td>24-01-1947</td>\n",
       "      <td>Nurse, learning disability</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Index          User Id First Name Last Name  Gender  \\\n",
       "0        1  8717bbf45cCDbEe     Shelia   Mahoney    Male   \n",
       "1        2  3d5AD30A4cD38ed         Jo    Rivers  Female   \n",
       "2        3  810Ce0F276Badec     Sheryl    Lowery  Female   \n",
       "3        4  BF2a889C00f0cE1    Whitney    Hooper    Male   \n",
       "4        5  9afFEafAe1CBBB9    Lindsey      Rice  Female   \n",
       "..     ...              ...        ...       ...     ...   \n",
       "995    996  fedF4c7Fd9e7cFa       Kurt    Bryant  Female   \n",
       "996    997  ECddaFEDdEc4FAB      Donna     Barry  Female   \n",
       "997    998  2adde51d8B8979E      Cathy  Mckinney  Female   \n",
       "998    999  Fb2FE369D1E171A   Jermaine    Phelps    Male   \n",
       "999   1000  8b756f6231DDC6e        Lee      Tran  Female   \n",
       "\n",
       "                             Email                  Phone Date of birth  \\\n",
       "0              pwarner@example.org           857.139.8239    27-01-2014   \n",
       "1    fergusonkatherine@example.net                    NaN    26-07-1931   \n",
       "2              fhoward@example.org          (599)782-0605    25-11-2013   \n",
       "3            zjohnston@example.com                    NaN    17-11-2012   \n",
       "4                 elin@example.net     (390)417-1635x3010    15-04-1923   \n",
       "..                             ...                    ...           ...   \n",
       "995         lyonsdaisy@example.net           021.775.2933    05-01-1959   \n",
       "996        dariusbryan@example.com   001-149-710-7799x721    06-10-2001   \n",
       "997         georgechan@example.org  +1-750-774-4128x33265    13-05-1918   \n",
       "998            wanda04@example.net          (915)292-2254    31-08-1971   \n",
       "999        deannablack@example.org     079.752.5424x67259    24-01-1947   \n",
       "\n",
       "                           Job Title  Salary  \n",
       "0                  Probation officer   90000  \n",
       "1                             Dancer   80000  \n",
       "2                               Copy   50000  \n",
       "3           Counselling psychologist   65000  \n",
       "4                Biomedical engineer  100000  \n",
       "..                               ...     ...  \n",
       "995                Personnel officer   90000  \n",
       "996          Education administrator   50000  \n",
       "997  Commercial/residential surveyor   60000  \n",
       "998                 Ambulance person  100000  \n",
       "999       Nurse, learning disability   90000  \n",
       "\n",
       "[1000 rows x 10 columns]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "479d4fa0-b1dd-40b7-baca-19751e02ad01",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>50</th>\n",
       "      <th>afF3018e9cdd1dA</th>\n",
       "      <th>George</th>\n",
       "      <th>Mercer</th>\n",
       "      <th>Female</th>\n",
       "      <th>douglascontreras@example.net</th>\n",
       "      <th>+1-326-669-0118x4341</th>\n",
       "      <th>11-09-1941</th>\n",
       "      <th>Human resources officer</th>\n",
       "      <th>70000</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>51</td>\n",
       "      <td>CccE5DAb6E288e5</td>\n",
       "      <td>Jo</td>\n",
       "      <td>Zavala</td>\n",
       "      <td>Male</td>\n",
       "      <td>pamela64@example.net</td>\n",
       "      <td>001-859-448-9935x54536</td>\n",
       "      <td>23-11-1992</td>\n",
       "      <td>Nurse, adult</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>52</td>\n",
       "      <td>DfBDc3621D4bcec</td>\n",
       "      <td>Joshua</td>\n",
       "      <td>Carey</td>\n",
       "      <td>Female</td>\n",
       "      <td>dianashepherd@example.net</td>\n",
       "      <td>001-274-739-8470x814</td>\n",
       "      <td>07-01-1915</td>\n",
       "      <td>Seismic interpreter</td>\n",
       "      <td>70000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>53</td>\n",
       "      <td>f55b0A249f5E44D</td>\n",
       "      <td>Rickey</td>\n",
       "      <td>Hobbs</td>\n",
       "      <td>Female</td>\n",
       "      <td>ingramtiffany@example.org</td>\n",
       "      <td>241.179.9509x498</td>\n",
       "      <td>01-07-1910</td>\n",
       "      <td>Barrister</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>54</td>\n",
       "      <td>Ed71DcfaBFd0beE</td>\n",
       "      <td>Robyn</td>\n",
       "      <td>Reilly</td>\n",
       "      <td>Male</td>\n",
       "      <td>carriecrawford@example.org</td>\n",
       "      <td>207.797.8345x6177</td>\n",
       "      <td>27-07-1982</td>\n",
       "      <td>Engineer, structural</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>55</td>\n",
       "      <td>FDaFD0c3f5387EC</td>\n",
       "      <td>Christina</td>\n",
       "      <td>Conrad</td>\n",
       "      <td>Male</td>\n",
       "      <td>fuentesclaudia@example.net</td>\n",
       "      <td>001-599-042-7428x143</td>\n",
       "      <td>06-01-1998</td>\n",
       "      <td>Producer, radio</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>945</th>\n",
       "      <td>996</td>\n",
       "      <td>fedF4c7Fd9e7cFa</td>\n",
       "      <td>Kurt</td>\n",
       "      <td>Bryant</td>\n",
       "      <td>Female</td>\n",
       "      <td>lyonsdaisy@example.net</td>\n",
       "      <td>021.775.2933</td>\n",
       "      <td>05-01-1959</td>\n",
       "      <td>Personnel officer</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>946</th>\n",
       "      <td>997</td>\n",
       "      <td>ECddaFEDdEc4FAB</td>\n",
       "      <td>Donna</td>\n",
       "      <td>Barry</td>\n",
       "      <td>Female</td>\n",
       "      <td>dariusbryan@example.com</td>\n",
       "      <td>001-149-710-7799x721</td>\n",
       "      <td>06-10-2001</td>\n",
       "      <td>Education administrator</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>947</th>\n",
       "      <td>998</td>\n",
       "      <td>2adde51d8B8979E</td>\n",
       "      <td>Cathy</td>\n",
       "      <td>Mckinney</td>\n",
       "      <td>Female</td>\n",
       "      <td>georgechan@example.org</td>\n",
       "      <td>+1-750-774-4128x33265</td>\n",
       "      <td>13-05-1918</td>\n",
       "      <td>Commercial/residential surveyor</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>948</th>\n",
       "      <td>999</td>\n",
       "      <td>Fb2FE369D1E171A</td>\n",
       "      <td>Jermaine</td>\n",
       "      <td>Phelps</td>\n",
       "      <td>Male</td>\n",
       "      <td>wanda04@example.net</td>\n",
       "      <td>(915)292-2254</td>\n",
       "      <td>31-08-1971</td>\n",
       "      <td>Ambulance person</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>949</th>\n",
       "      <td>1000</td>\n",
       "      <td>8b756f6231DDC6e</td>\n",
       "      <td>Lee</td>\n",
       "      <td>Tran</td>\n",
       "      <td>Female</td>\n",
       "      <td>deannablack@example.org</td>\n",
       "      <td>079.752.5424x67259</td>\n",
       "      <td>24-01-1947</td>\n",
       "      <td>Nurse, learning disability</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>950 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       50  afF3018e9cdd1dA     George    Mercer  Female  \\\n",
       "0      51  CccE5DAb6E288e5         Jo    Zavala    Male   \n",
       "1      52  DfBDc3621D4bcec     Joshua     Carey  Female   \n",
       "2      53  f55b0A249f5E44D     Rickey     Hobbs  Female   \n",
       "3      54  Ed71DcfaBFd0beE      Robyn    Reilly    Male   \n",
       "4      55  FDaFD0c3f5387EC  Christina    Conrad    Male   \n",
       "..    ...              ...        ...       ...     ...   \n",
       "945   996  fedF4c7Fd9e7cFa       Kurt    Bryant  Female   \n",
       "946   997  ECddaFEDdEc4FAB      Donna     Barry  Female   \n",
       "947   998  2adde51d8B8979E      Cathy  Mckinney  Female   \n",
       "948   999  Fb2FE369D1E171A   Jermaine    Phelps    Male   \n",
       "949  1000  8b756f6231DDC6e        Lee      Tran  Female   \n",
       "\n",
       "    douglascontreras@example.net    +1-326-669-0118x4341  11-09-1941  \\\n",
       "0           pamela64@example.net  001-859-448-9935x54536  23-11-1992   \n",
       "1      dianashepherd@example.net    001-274-739-8470x814  07-01-1915   \n",
       "2      ingramtiffany@example.org        241.179.9509x498  01-07-1910   \n",
       "3     carriecrawford@example.org       207.797.8345x6177  27-07-1982   \n",
       "4     fuentesclaudia@example.net    001-599-042-7428x143  06-01-1998   \n",
       "..                           ...                     ...         ...   \n",
       "945       lyonsdaisy@example.net            021.775.2933  05-01-1959   \n",
       "946      dariusbryan@example.com    001-149-710-7799x721  06-10-2001   \n",
       "947       georgechan@example.org   +1-750-774-4128x33265  13-05-1918   \n",
       "948          wanda04@example.net           (915)292-2254  31-08-1971   \n",
       "949      deannablack@example.org      079.752.5424x67259  24-01-1947   \n",
       "\n",
       "             Human resources officer   70000  \n",
       "0                       Nurse, adult   80000  \n",
       "1                Seismic interpreter   70000  \n",
       "2                          Barrister   60000  \n",
       "3               Engineer, structural  100000  \n",
       "4                    Producer, radio   50000  \n",
       "..                               ...     ...  \n",
       "945                Personnel officer   90000  \n",
       "946          Education administrator   50000  \n",
       "947  Commercial/residential surveyor   60000  \n",
       "948                 Ambulance person  100000  \n",
       "949       Nurse, learning disability   90000  \n",
       "\n",
       "[950 rows x 10 columns]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#for skipping 50 rows\n",
    "df_skip50=pd.read_csv('People Data.csv',skiprows=50)\n",
    "df_skip50"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "b86ee180-8e64-49c0-a0d6-f2e03e62a096",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Last Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Email</th>\n",
       "      <th>Phone</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mahoney</td>\n",
       "      <td>Male</td>\n",
       "      <td>pwarner@example.org</td>\n",
       "      <td>857.139.8239</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Rivers</td>\n",
       "      <td>Female</td>\n",
       "      <td>fergusonkatherine@example.net</td>\n",
       "      <td>NaN</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Lowery</td>\n",
       "      <td>Female</td>\n",
       "      <td>fhoward@example.org</td>\n",
       "      <td>(599)782-0605</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hooper</td>\n",
       "      <td>Male</td>\n",
       "      <td>zjohnston@example.com</td>\n",
       "      <td>NaN</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Rice</td>\n",
       "      <td>Female</td>\n",
       "      <td>elin@example.net</td>\n",
       "      <td>(390)417-1635x3010</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>Bryant</td>\n",
       "      <td>Female</td>\n",
       "      <td>lyonsdaisy@example.net</td>\n",
       "      <td>021.775.2933</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>Barry</td>\n",
       "      <td>Female</td>\n",
       "      <td>dariusbryan@example.com</td>\n",
       "      <td>001-149-710-7799x721</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>Mckinney</td>\n",
       "      <td>Female</td>\n",
       "      <td>georgechan@example.org</td>\n",
       "      <td>+1-750-774-4128x33265</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>Phelps</td>\n",
       "      <td>Male</td>\n",
       "      <td>wanda04@example.net</td>\n",
       "      <td>(915)292-2254</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>Tran</td>\n",
       "      <td>Female</td>\n",
       "      <td>deannablack@example.org</td>\n",
       "      <td>079.752.5424x67259</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Last Name  Gender                          Email                  Phone  \\\n",
       "0     Mahoney    Male            pwarner@example.org           857.139.8239   \n",
       "1      Rivers  Female  fergusonkatherine@example.net                    NaN   \n",
       "2      Lowery  Female            fhoward@example.org          (599)782-0605   \n",
       "3      Hooper    Male          zjohnston@example.com                    NaN   \n",
       "4        Rice  Female               elin@example.net     (390)417-1635x3010   \n",
       "..        ...     ...                            ...                    ...   \n",
       "995    Bryant  Female         lyonsdaisy@example.net           021.775.2933   \n",
       "996     Barry  Female        dariusbryan@example.com   001-149-710-7799x721   \n",
       "997  Mckinney  Female         georgechan@example.org  +1-750-774-4128x33265   \n",
       "998    Phelps    Male            wanda04@example.net          (915)292-2254   \n",
       "999      Tran  Female        deannablack@example.org     079.752.5424x67259   \n",
       "\n",
       "     Salary  \n",
       "0     90000  \n",
       "1     80000  \n",
       "2     50000  \n",
       "3     65000  \n",
       "4    100000  \n",
       "..      ...  \n",
       "995   90000  \n",
       "996   50000  \n",
       "997   60000  \n",
       "998  100000  \n",
       "999   90000  \n",
       "\n",
       "[1000 rows x 5 columns]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#b) Only read the columns: 'Last Name', ‘Gender’,’Email’,‘Phone’ and ‘Salary’ from the file\n",
    "df=pd.read_csv('People Data.csv',usecols=['Last Name','Gender','Email','Phone','Salary'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "343983fe-a7f0-4bdc-8645-099a256ba738",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Index</th>\n",
       "      <th>User Id</th>\n",
       "      <th>First Name</th>\n",
       "      <th>Last Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Email</th>\n",
       "      <th>Phone</th>\n",
       "      <th>Date of birth</th>\n",
       "      <th>Job Title</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>8717bbf45cCDbEe</td>\n",
       "      <td>Shelia</td>\n",
       "      <td>Mahoney</td>\n",
       "      <td>Male</td>\n",
       "      <td>pwarner@example.org</td>\n",
       "      <td>857.139.8239</td>\n",
       "      <td>27-01-2014</td>\n",
       "      <td>Probation officer</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>3d5AD30A4cD38ed</td>\n",
       "      <td>Jo</td>\n",
       "      <td>Rivers</td>\n",
       "      <td>Female</td>\n",
       "      <td>fergusonkatherine@example.net</td>\n",
       "      <td>NaN</td>\n",
       "      <td>26-07-1931</td>\n",
       "      <td>Dancer</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>810Ce0F276Badec</td>\n",
       "      <td>Sheryl</td>\n",
       "      <td>Lowery</td>\n",
       "      <td>Female</td>\n",
       "      <td>fhoward@example.org</td>\n",
       "      <td>(599)782-0605</td>\n",
       "      <td>25-11-2013</td>\n",
       "      <td>Copy</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>BF2a889C00f0cE1</td>\n",
       "      <td>Whitney</td>\n",
       "      <td>Hooper</td>\n",
       "      <td>Male</td>\n",
       "      <td>zjohnston@example.com</td>\n",
       "      <td>NaN</td>\n",
       "      <td>17-11-2012</td>\n",
       "      <td>Counselling psychologist</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>9afFEafAe1CBBB9</td>\n",
       "      <td>Lindsey</td>\n",
       "      <td>Rice</td>\n",
       "      <td>Female</td>\n",
       "      <td>elin@example.net</td>\n",
       "      <td>(390)417-1635x3010</td>\n",
       "      <td>15-04-1923</td>\n",
       "      <td>Biomedical engineer</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>aF75e6dDEBC5b66</td>\n",
       "      <td>Sherry</td>\n",
       "      <td>Caldwell</td>\n",
       "      <td>Male</td>\n",
       "      <td>kaitlin13@example.net</td>\n",
       "      <td>8537800927</td>\n",
       "      <td>06-08-1917</td>\n",
       "      <td>Higher education lecturer</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>efeb05c7Cc94EA3</td>\n",
       "      <td>Ernest</td>\n",
       "      <td>Hoffman</td>\n",
       "      <td>Male</td>\n",
       "      <td>jeffharvey@example.com</td>\n",
       "      <td>093.655.7480x7895</td>\n",
       "      <td>22-12-1984</td>\n",
       "      <td>Health visitor</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>fb1BF3FED57E9d7</td>\n",
       "      <td>Doris</td>\n",
       "      <td>Andersen</td>\n",
       "      <td>Male</td>\n",
       "      <td>alicia33@example.org</td>\n",
       "      <td>4709522945</td>\n",
       "      <td>02-12-2016</td>\n",
       "      <td>Air broker</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>421fAB9a3b98F30</td>\n",
       "      <td>Cheryl</td>\n",
       "      <td>Mays</td>\n",
       "      <td>Male</td>\n",
       "      <td>jake50@example.com</td>\n",
       "      <td>013.820.4758</td>\n",
       "      <td>16-12-2012</td>\n",
       "      <td>Designer, multimedia</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>4A42Fe10dB717CB</td>\n",
       "      <td>Harry</td>\n",
       "      <td>Mitchell</td>\n",
       "      <td>Male</td>\n",
       "      <td>lanechristina@example.net</td>\n",
       "      <td>(560)903-5068x4985</td>\n",
       "      <td>29-06-1953</td>\n",
       "      <td>Insurance account manager</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Index          User Id First Name Last Name  Gender  \\\n",
       "0      1  8717bbf45cCDbEe     Shelia   Mahoney    Male   \n",
       "1      2  3d5AD30A4cD38ed         Jo    Rivers  Female   \n",
       "2      3  810Ce0F276Badec     Sheryl    Lowery  Female   \n",
       "3      4  BF2a889C00f0cE1    Whitney    Hooper    Male   \n",
       "4      5  9afFEafAe1CBBB9    Lindsey      Rice  Female   \n",
       "5      6  aF75e6dDEBC5b66     Sherry  Caldwell    Male   \n",
       "6      7  efeb05c7Cc94EA3     Ernest   Hoffman    Male   \n",
       "7      8  fb1BF3FED57E9d7      Doris  Andersen    Male   \n",
       "8      9  421fAB9a3b98F30     Cheryl      Mays    Male   \n",
       "9     10  4A42Fe10dB717CB      Harry  Mitchell    Male   \n",
       "\n",
       "                           Email               Phone Date of birth  \\\n",
       "0            pwarner@example.org        857.139.8239    27-01-2014   \n",
       "1  fergusonkatherine@example.net                 NaN    26-07-1931   \n",
       "2            fhoward@example.org       (599)782-0605    25-11-2013   \n",
       "3          zjohnston@example.com                 NaN    17-11-2012   \n",
       "4               elin@example.net  (390)417-1635x3010    15-04-1923   \n",
       "5          kaitlin13@example.net          8537800927    06-08-1917   \n",
       "6         jeffharvey@example.com   093.655.7480x7895    22-12-1984   \n",
       "7           alicia33@example.org          4709522945    02-12-2016   \n",
       "8             jake50@example.com        013.820.4758    16-12-2012   \n",
       "9      lanechristina@example.net  (560)903-5068x4985    29-06-1953   \n",
       "\n",
       "                   Job Title  Salary  \n",
       "0          Probation officer   90000  \n",
       "1                     Dancer   80000  \n",
       "2                       Copy   50000  \n",
       "3   Counselling psychologist   65000  \n",
       "4        Biomedical engineer  100000  \n",
       "5  Higher education lecturer   50000  \n",
       "6             Health visitor   60000  \n",
       "7                 Air broker   65000  \n",
       "8       Designer, multimedia   50000  \n",
       "9  Insurance account manager   50000  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#c) Display the first 10 rows of the filtered dataset.\n",
    "\n",
    "df=pd.read_csv('People Data.csv',nrows=10)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "74428c69-8de9-461e-9644-94b5a23171bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Salary\n",
       "995   90000\n",
       "996   50000\n",
       "997   60000\n",
       "998  100000\n",
       "999   90000"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#d) Extract the ‘Salary’' column as a Series and display its last 5 valuesX\n",
    "\n",
    "df=pd.read_csv('People Data.csv' ,usecols=['Salary']  )\n",
    "df.tail(5)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40a6e17b-67ae-4423-954a-2cd3897d657c",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "14c6eb1f-4424-4504-b70b-c09460760a8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#question 9\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5826d5ea-131f-4a70-9e43-90c356a7833c",
   "metadata": {},
   "outputs": [],
   "source": [
    " \n",
    "# Filter and select rows from the People_Dataset, where the “Last Name' column contains the name 'DuKe', \n",
    "#'Gender' column contains the word Female and ‘Salary’ should Pe less than 85000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "89a7f2b5-dfbf-4888-9c09-6281a7188343",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Index</th>\n",
       "      <th>User Id</th>\n",
       "      <th>First Name</th>\n",
       "      <th>Last Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Email</th>\n",
       "      <th>Phone</th>\n",
       "      <th>Date of birth</th>\n",
       "      <th>Job Title</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>46</td>\n",
       "      <td>99A502C175C4EBd</td>\n",
       "      <td>Olivia</td>\n",
       "      <td>Duke</td>\n",
       "      <td>Female</td>\n",
       "      <td>diana26@example.net</td>\n",
       "      <td>001-366-475-8607x04350</td>\n",
       "      <td>13-10-1934</td>\n",
       "      <td>Dentist</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>210</th>\n",
       "      <td>211</td>\n",
       "      <td>DF17975CC0a0373</td>\n",
       "      <td>Katrina</td>\n",
       "      <td>Duke</td>\n",
       "      <td>Female</td>\n",
       "      <td>robin78@example.com</td>\n",
       "      <td>740.434.0212</td>\n",
       "      <td>21-09-1935</td>\n",
       "      <td>Producer, radio</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>457</th>\n",
       "      <td>458</td>\n",
       "      <td>dcE1B7DE83c1076</td>\n",
       "      <td>Traci</td>\n",
       "      <td>Duke</td>\n",
       "      <td>Female</td>\n",
       "      <td>perryhoffman@example.org</td>\n",
       "      <td>+1-903-596-0995x489</td>\n",
       "      <td>11-02-1997</td>\n",
       "      <td>Herbalist</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>729</th>\n",
       "      <td>730</td>\n",
       "      <td>c9b482D7aa3e682</td>\n",
       "      <td>Lonnie</td>\n",
       "      <td>Duke</td>\n",
       "      <td>Female</td>\n",
       "      <td>kevinkramer@example.net</td>\n",
       "      <td>982.692.6257</td>\n",
       "      <td>12-05-2015</td>\n",
       "      <td>Nurse, adult</td>\n",
       "      <td>70000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Index          User Id First Name Last Name  Gender  \\\n",
       "45      46  99A502C175C4EBd     Olivia      Duke  Female   \n",
       "210    211  DF17975CC0a0373    Katrina      Duke  Female   \n",
       "457    458  dcE1B7DE83c1076      Traci      Duke  Female   \n",
       "729    730  c9b482D7aa3e682     Lonnie      Duke  Female   \n",
       "\n",
       "                        Email                   Phone Date of birth  \\\n",
       "45        diana26@example.net  001-366-475-8607x04350    13-10-1934   \n",
       "210       robin78@example.com            740.434.0212    21-09-1935   \n",
       "457  perryhoffman@example.org     +1-903-596-0995x489    11-02-1997   \n",
       "729   kevinkramer@example.net            982.692.6257    12-05-2015   \n",
       "\n",
       "           Job Title  Salary  \n",
       "45           Dentist   60000  \n",
       "210  Producer, radio   50000  \n",
       "457        Herbalist   50000  \n",
       "729     Nurse, adult   70000  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "#READ DATA SET\n",
    "df=pd.read_csv('People Data.csv')\n",
    "\n",
    "row=df[(df['Last Name'].str.contains('Duke'))   &(df['Gender']==('Female'))   &(df['Salary']<85000)]\n",
    "\n",
    "row\n",
    "                                             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "359486de-3478-467d-9ead-990039dd6acd",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5bef74b0-42e8-4da3-9279-2be60cdd2f42",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "018d922f-254a-40ec-baf5-159238df9b5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a 7*5 Dataframe in Pandas using a series generated from 35 random integers Petween 1 to 6)?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "cf206fd3-0559-409f-a232-16f152142645",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   0  1  2  3  4\n",
       "0  6  4  3  3  4\n",
       "1  2  3  4  1  3\n",
       "2  5  3  4  4  1\n",
       "3  5  2  3  3  2\n",
       "4  4  1  6  2  3\n",
       "5  2  5  1  6  3\n",
       "6  6  2  5  4  4"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "#generate a random array between 1 to 6\n",
    "arr=np.random.randint(1,7, 35)\n",
    "\n",
    "series=pd.Series(arr)\n",
    "\n",
    "data_frame = pd.DataFrame(series.values.reshape(7,5))\n",
    "\n",
    "data_frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65d3de53-dacd-42aa-8433-d274f40e2e43",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "edf649c3-b932-462a-8c4d-e3edc3029c8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 11\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "057fb69a-b5b1-43b1-89c7-d9a73086d5a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     27\n",
       "1     19\n",
       "2     19\n",
       "3     38\n",
       "4     43\n",
       "5     40\n",
       "6     14\n",
       "7     46\n",
       "8     18\n",
       "9     45\n",
       "10    41\n",
       "11    29\n",
       "12    30\n",
       "13    45\n",
       "14    17\n",
       "15    35\n",
       "16    26\n",
       "17    26\n",
       "18    10\n",
       "19    39\n",
       "20    47\n",
       "21    32\n",
       "22    39\n",
       "23    41\n",
       "24    17\n",
       "25    42\n",
       "26    37\n",
       "27    35\n",
       "28    42\n",
       "29    13\n",
       "30    37\n",
       "31    42\n",
       "32    23\n",
       "33    13\n",
       "34    30\n",
       "35    24\n",
       "36    14\n",
       "37    39\n",
       "38    25\n",
       "39    30\n",
       "40    31\n",
       "41    33\n",
       "42    43\n",
       "43    50\n",
       "44    25\n",
       "45    11\n",
       "46    23\n",
       "47    13\n",
       "48    45\n",
       "49    22\n",
       "Name: col1, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create two different Series, each of length 50, with the following criteria:\n",
    "\n",
    "\n",
    "#a) The first Series should contain random numbers ranging from 10 to 50\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "series1=pd.Series(np.random.randint(10,51, size=50) ,name='col1')\n",
    "\n",
    "series1                 \n",
    "                  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d47d35e9-2e49-4e8e-ba7e-0b5da2bcef99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     133\n",
       "1     785\n",
       "2     836\n",
       "3     852\n",
       "4     568\n",
       "5     711\n",
       "6     586\n",
       "7     774\n",
       "8     546\n",
       "9     532\n",
       "10    379\n",
       "11    295\n",
       "12    614\n",
       "13    281\n",
       "14    140\n",
       "15    861\n",
       "16    488\n",
       "17    470\n",
       "18    272\n",
       "19    198\n",
       "20    636\n",
       "21    469\n",
       "22    291\n",
       "23    760\n",
       "24    673\n",
       "25    647\n",
       "26    898\n",
       "27    581\n",
       "28    555\n",
       "29    653\n",
       "30    487\n",
       "31    857\n",
       "32    974\n",
       "33    650\n",
       "34    939\n",
       "35    658\n",
       "36    748\n",
       "37    813\n",
       "38    660\n",
       "39    772\n",
       "40    614\n",
       "41    855\n",
       "42    140\n",
       "43    585\n",
       "44    641\n",
       "45    516\n",
       "46    399\n",
       "47    626\n",
       "48    886\n",
       "49    173\n",
       "Name: col2, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "\n",
    "#b) The second Series should contain random numbers ranging from 100 to 1000.\n",
    "\n",
    "import numpy as nnp\n",
    "import pandas as pd\n",
    "\n",
    "arr=np.random.randint(100,1001,size=50)\n",
    "series2=pd.Series(arr,name='col2')\n",
    "series2\n",
    "                 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3a0c4dd3-a86e-4977-88bc-e8032b17edea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>27</td>\n",
       "      <td>133</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>19</td>\n",
       "      <td>785</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>19</td>\n",
       "      <td>836</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>38</td>\n",
       "      <td>852</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>43</td>\n",
       "      <td>568</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>40</td>\n",
       "      <td>711</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>14</td>\n",
       "      <td>586</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>46</td>\n",
       "      <td>774</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>18</td>\n",
       "      <td>546</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>45</td>\n",
       "      <td>532</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>41</td>\n",
       "      <td>379</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>29</td>\n",
       "      <td>295</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>30</td>\n",
       "      <td>614</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>45</td>\n",
       "      <td>281</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>17</td>\n",
       "      <td>140</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>35</td>\n",
       "      <td>861</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>26</td>\n",
       "      <td>488</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>26</td>\n",
       "      <td>470</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>10</td>\n",
       "      <td>272</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>39</td>\n",
       "      <td>198</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>47</td>\n",
       "      <td>636</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>32</td>\n",
       "      <td>469</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>39</td>\n",
       "      <td>291</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>41</td>\n",
       "      <td>760</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>17</td>\n",
       "      <td>673</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>42</td>\n",
       "      <td>647</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>37</td>\n",
       "      <td>898</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>35</td>\n",
       "      <td>581</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>42</td>\n",
       "      <td>555</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>13</td>\n",
       "      <td>653</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>37</td>\n",
       "      <td>487</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>42</td>\n",
       "      <td>857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>23</td>\n",
       "      <td>974</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>13</td>\n",
       "      <td>650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>30</td>\n",
       "      <td>939</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>24</td>\n",
       "      <td>658</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>14</td>\n",
       "      <td>748</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>39</td>\n",
       "      <td>813</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>25</td>\n",
       "      <td>660</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>30</td>\n",
       "      <td>772</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>31</td>\n",
       "      <td>614</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>33</td>\n",
       "      <td>855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>43</td>\n",
       "      <td>140</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>50</td>\n",
       "      <td>585</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>25</td>\n",
       "      <td>641</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>11</td>\n",
       "      <td>516</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>23</td>\n",
       "      <td>399</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>13</td>\n",
       "      <td>626</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>45</td>\n",
       "      <td>886</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>22</td>\n",
       "      <td>173</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    col1  col2\n",
       "0     27   133\n",
       "1     19   785\n",
       "2     19   836\n",
       "3     38   852\n",
       "4     43   568\n",
       "5     40   711\n",
       "6     14   586\n",
       "7     46   774\n",
       "8     18   546\n",
       "9     45   532\n",
       "10    41   379\n",
       "11    29   295\n",
       "12    30   614\n",
       "13    45   281\n",
       "14    17   140\n",
       "15    35   861\n",
       "16    26   488\n",
       "17    26   470\n",
       "18    10   272\n",
       "19    39   198\n",
       "20    47   636\n",
       "21    32   469\n",
       "22    39   291\n",
       "23    41   760\n",
       "24    17   673\n",
       "25    42   647\n",
       "26    37   898\n",
       "27    35   581\n",
       "28    42   555\n",
       "29    13   653\n",
       "30    37   487\n",
       "31    42   857\n",
       "32    23   974\n",
       "33    13   650\n",
       "34    30   939\n",
       "35    24   658\n",
       "36    14   748\n",
       "37    39   813\n",
       "38    25   660\n",
       "39    30   772\n",
       "40    31   614\n",
       "41    33   855\n",
       "42    43   140\n",
       "43    50   585\n",
       "44    25   641\n",
       "45    11   516\n",
       "46    23   399\n",
       "47    13   626\n",
       "48    45   886\n",
       "49    22   173"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_frame=pd.concat([series1,series2] ,axis=1)\n",
    "data_frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3380234-2813-4793-9a2b-a18caadc45f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "72e17481-9d06-4a16-85ea-e6ed672dadda",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 12\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ed9d3cb0-e6fd-4e01-8ab1-e6ddcee4b799",
   "metadata": {},
   "outputs": [],
   "source": [
    "#K%g Perform the following operations using people data set:\n",
    "\n",
    "#a) Delete the 'Email', 'Phone', and 'Date of birth' columns from the dataset.\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "data=pd.read_csv('People Data.csv')\n",
    "\n",
    "data.drop(['Email','Phone','Date of birth'],axis=1,inplace=True)\n",
    "\n",
    "\n",
    "#b) Delete the rows containing any missing values.\n",
    "\n",
    "data.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2c7245da-fa9f-49d5-a304-1af2de3f3d14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Index</th>\n",
       "      <th>User Id</th>\n",
       "      <th>First Name</th>\n",
       "      <th>Last Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Job Title</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>8717bbf45cCDbEe</td>\n",
       "      <td>Shelia</td>\n",
       "      <td>Mahoney</td>\n",
       "      <td>Male</td>\n",
       "      <td>Probation officer</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>3d5AD30A4cD38ed</td>\n",
       "      <td>Jo</td>\n",
       "      <td>Rivers</td>\n",
       "      <td>Female</td>\n",
       "      <td>Dancer</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>810Ce0F276Badec</td>\n",
       "      <td>Sheryl</td>\n",
       "      <td>Lowery</td>\n",
       "      <td>Female</td>\n",
       "      <td>Copy</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>BF2a889C00f0cE1</td>\n",
       "      <td>Whitney</td>\n",
       "      <td>Hooper</td>\n",
       "      <td>Male</td>\n",
       "      <td>Counselling psychologist</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>9afFEafAe1CBBB9</td>\n",
       "      <td>Lindsey</td>\n",
       "      <td>Rice</td>\n",
       "      <td>Female</td>\n",
       "      <td>Biomedical engineer</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>996</td>\n",
       "      <td>fedF4c7Fd9e7cFa</td>\n",
       "      <td>Kurt</td>\n",
       "      <td>Bryant</td>\n",
       "      <td>Female</td>\n",
       "      <td>Personnel officer</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>997</td>\n",
       "      <td>ECddaFEDdEc4FAB</td>\n",
       "      <td>Donna</td>\n",
       "      <td>Barry</td>\n",
       "      <td>Female</td>\n",
       "      <td>Education administrator</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>998</td>\n",
       "      <td>2adde51d8B8979E</td>\n",
       "      <td>Cathy</td>\n",
       "      <td>Mckinney</td>\n",
       "      <td>Female</td>\n",
       "      <td>Commercial/residential surveyor</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>999</td>\n",
       "      <td>Fb2FE369D1E171A</td>\n",
       "      <td>Jermaine</td>\n",
       "      <td>Phelps</td>\n",
       "      <td>Male</td>\n",
       "      <td>Ambulance person</td>\n",
       "      <td>100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>1000</td>\n",
       "      <td>8b756f6231DDC6e</td>\n",
       "      <td>Lee</td>\n",
       "      <td>Tran</td>\n",
       "      <td>Female</td>\n",
       "      <td>Nurse, learning disability</td>\n",
       "      <td>90000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Index          User Id First Name Last Name  Gender  \\\n",
       "0        1  8717bbf45cCDbEe     Shelia   Mahoney    Male   \n",
       "1        2  3d5AD30A4cD38ed         Jo    Rivers  Female   \n",
       "2        3  810Ce0F276Badec     Sheryl    Lowery  Female   \n",
       "3        4  BF2a889C00f0cE1    Whitney    Hooper    Male   \n",
       "4        5  9afFEafAe1CBBB9    Lindsey      Rice  Female   \n",
       "..     ...              ...        ...       ...     ...   \n",
       "995    996  fedF4c7Fd9e7cFa       Kurt    Bryant  Female   \n",
       "996    997  ECddaFEDdEc4FAB      Donna     Barry  Female   \n",
       "997    998  2adde51d8B8979E      Cathy  Mckinney  Female   \n",
       "998    999  Fb2FE369D1E171A   Jermaine    Phelps    Male   \n",
       "999   1000  8b756f6231DDC6e        Lee      Tran  Female   \n",
       "\n",
       "                           Job Title  Salary  \n",
       "0                  Probation officer   90000  \n",
       "1                             Dancer   80000  \n",
       "2                               Copy   50000  \n",
       "3           Counselling psychologist   65000  \n",
       "4                Biomedical engineer  100000  \n",
       "..                               ...     ...  \n",
       "995                Personnel officer   90000  \n",
       "996          Education administrator   50000  \n",
       "997  Commercial/residential surveyor   60000  \n",
       "998                 Ambulance person  100000  \n",
       "999       Nurse, learning disability   90000  \n",
       "\n",
       "[1000 rows x 7 columns]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "\n",
    "#c) Print the final output also\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70129c67-1296-47d0-a9f4-7257fbb89693",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "46d52855-ee1c-4652-8091-14daff37628b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION 13  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "18fa4dbc-e9ef-44a8-b8d8-b46476ffacb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#g Create two NumPy arrays, x and y, each containing 100 random float values between 0 and 1. Perform the following tasks using Matplotlib and NumPy:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2ea8c46c-a878-4491-8387-c2484c37592a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.11521898, 0.09492561, 0.57720186, 0.1936267 , 0.56602504,\n",
       "       0.06115003, 0.00881554, 0.22151978, 0.88909549, 0.60428482,\n",
       "       0.12062596, 0.74728517, 0.52586601, 0.62373912, 0.67722035,\n",
       "       0.89657561, 0.79651892, 0.70306689, 0.34224978, 0.35216413,\n",
       "       0.23854016, 0.28629569, 0.42531793, 0.14499692, 0.8724399 ,\n",
       "       0.91113597, 0.67826377, 0.92529158, 0.19371165, 0.488085  ,\n",
       "       0.23036546, 0.73115267, 0.76310436, 0.52681183, 0.82724986,\n",
       "       0.45187694, 0.37379577, 0.89163816, 0.03483881, 0.69483213,\n",
       "       0.52968773, 0.68429965, 0.7597706 , 0.77151127, 0.3515668 ,\n",
       "       0.28181023, 0.62776459, 0.12829327, 0.35290793, 0.84235241,\n",
       "       0.48131436, 0.40544242, 0.37684547, 0.10630748, 0.92995775,\n",
       "       0.19775671, 0.7582222 , 0.40542969, 0.25084747, 0.65249427,\n",
       "       0.07824967, 0.08195657, 0.53338205, 0.35750189, 0.52105143,\n",
       "       0.70202875, 0.40454254, 0.19583683, 0.87132847, 0.68752591,\n",
       "       0.16774271, 0.16002547, 0.01952255, 0.25802233, 0.00880385,\n",
       "       0.98918717, 0.74820562, 0.6337491 , 0.86135614, 0.57653093,\n",
       "       0.50168023, 0.93301546, 0.89339185, 0.64056099, 0.36456128,\n",
       "       0.79519222, 0.73767135, 0.90683864, 0.21535201, 0.34169487,\n",
       "       0.76526711, 0.4244879 , 0.9183032 , 0.81666928, 0.79554567,\n",
       "       0.03189261, 0.77137772, 0.26784441, 0.17880748, 0.28617471])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "#generate random value for x\n",
    "x=np.random.rand(100)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c2c66a25-44d0-49ae-88d6-91288d0f67ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.72520857, 0.54785951, 0.95380292, 0.80590055, 0.93282132,\n",
       "       0.42091211, 0.12909651, 0.53895158, 0.37971531, 0.91681998,\n",
       "       0.66180536, 0.91971018, 0.67249943, 0.19105111, 0.08125217,\n",
       "       0.73467644, 0.16424049, 0.23559133, 0.75319815, 0.74827981,\n",
       "       0.51999346, 0.40703322, 0.63696167, 0.46685346, 0.29892302,\n",
       "       0.24202032, 0.54725295, 0.16787184, 0.31558123, 0.17095108,\n",
       "       0.06820672, 0.06075036, 0.0584027 , 0.13231475, 0.41359612,\n",
       "       0.31531212, 0.24320844, 0.81434922, 0.4046859 , 0.73243451,\n",
       "       0.89501812, 0.82671824, 0.57844112, 0.57980513, 0.47439631,\n",
       "       0.62498707, 0.87483129, 0.31375279, 0.28084976, 0.51670567,\n",
       "       0.06522104, 0.19898754, 0.69917496, 0.81462773, 0.0042878 ,\n",
       "       0.77430565, 0.34019676, 0.79109856, 0.14383422, 0.15999638,\n",
       "       0.02854362, 0.34464986, 0.43742112, 0.69620045, 0.451071  ,\n",
       "       0.69355864, 0.01423879, 0.80894004, 0.26809765, 0.16477087,\n",
       "       0.65023277, 0.41737837, 0.6871975 , 0.63143695, 0.64730804,\n",
       "       0.75066654, 0.84703028, 0.63091318, 0.73001189, 0.73700407,\n",
       "       0.35475778, 0.44225068, 0.11908717, 0.05667697, 0.88274567,\n",
       "       0.54079707, 0.47548157, 0.19715726, 0.54841103, 0.89790169,\n",
       "       0.21004871, 0.29136878, 0.44091715, 0.1249818 , 0.59263149,\n",
       "       0.29951804, 0.02032715, 0.74384478, 0.87758671, 0.32676216])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#generate random number for y\n",
    "\n",
    "y=np.random.rand(100)\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b24c84d0-8a19-41fc-9f40-dc81cc1bebcf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x7ff7d4e91990>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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jh07dPHFFwfVPOO4vd7ZbFYrV67U448/rssvvzys5hnHy/v77NmzymQy2r59u6655hrdeuutevrpp/Xiiy8yOuKSl+t98OBBrV69Wo8++qgOHDigV199Vb29vWpqagqjqakUZH9pzO3SzJkzVVZWNi6KPnHixLhoznHJJZfkPb+8vFwzZswIrK0mKOV6O3bs2KH7779fL730km688cYgm2kMr9d7ZGRE+/fvV09Pj771rW9JsjtLy7JUXl6u1157TTfccEMobU+iUt7fs2bN0pw5c3K2S1+wYIEsy9KxY8d02WWXBdrmJCvlejc3N+u6667Tww8/LEn64he/qAsuuED19fV68sknGdn2WdD9pTEjI9OmTVNdXZ06Oztzjnd2dmrx4sV5n7No0aJx57/22mtauHChpk6dGlhbTVDK9ZbsEZF7771Xra2tzO164PV6T58+Xb/97W/11ltvjf40NTXpb/7mb/TWW2/p2muvDavpiVTK+/u6667Tu+++qw8++GD02Ntvv60pU6aopqYm0PYmXSnX+6OPPtKUKbldWFlZmaRP7tjhn8D7S1/SYGPCWRq2detW6+DBg9batWutCy64wDpy5IhlWZb1yCOPWHfffffo+c5SpXXr1lkHDx60tm7dytJeD7xe79bWVqu8vNx69tlnrf7+/tGf999/P6qXkCher/dYrKbxxuv1HhkZsWpqaqxly5ZZv/vd76zXX3/duuyyy6wHHnggqpeQKF6v9wsvvGCVl5dbLS0t1jvvvGO98cYb1sKFC61rrrkmqpeQKCMjI1ZPT4/V09NjSbKefvppq6enZ3Qpddj9pVHBiGVZ1rPPPmvNnTvXmjZtmnX11Vdbr7/++ujf3XPPPdaXv/zlnPO7u7utv/3bv7WmTZtmzZs3z9qyZUvILU42L9f7y1/+siVp3M8999wTfsMTyuv7+1wEI955vd6HDh2ybrzxRuu8886zampqrPXr11sfffRRyK1OLq/Xe/PmzdbnP/9567zzzrNmzZplfe1rX7OOHTsWcquTqaura8Lv47D7y4xlMZ4FAACiY0zOCAAASCaCEQAAECmCEQAAECmCEQAAECmCEQAAECmCEQAAECmCEQAAECmCEQAAECmCEQAAECmCEQAAECmCEQAAECmCEQAAEKn/D9oyU8Fb+y8yAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    " #Create a scatter \u0018lot using x and y, setting the color of the \u0018oints to red and the marker style to 'o'.\n",
    "import matplotlib.pyplot as plt\n",
    "plt.scatter(x,y ,color = 'red',marker='o',label='random points')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "af66ba3a-795a-4f0d-85c0-1ed4251ec207",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.lines.Line2D at 0x7ff7d4ae4d00>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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++KUV155JQoKCuJLX/rS8C5wDMn1XHR1dcXatWujoqIiioqK4rOf/Wxs3rz5HK12dMv1XGzZsiWuuOKKmDhxYpSXl8ctt9wSR44cOUerHb1eeumluO6662Lq1KmRl5cXzz333J89Zkgeu4fstx59Av/+7/+ejR8/PvvpT3+a7du3L7vjjjuySZMmZW+99Va/8wcOHMgmTpyY3XHHHdm+ffuyn/70p9n48eOzp59++hyvfPTJ9Vzccccd2fe///3stddey954441szZo12fjx47P//d//PccrH31yPRenvPfee9nMmTOzmpqa7Iorrjg3ix3lBnMuvvGNb2Tz5s3LGhoasoMHD2b//d//nb3yyivncNWjU67norGxMRs3blz2wx/+MDtw4EDW2NiYfeELX8iWLFlyjlc++mzfvj1bu3Zt9swzz2QRkT377LNnnB+qx+7zIlzmzp2b1dbW9tr3+c9/Prv77rv7nf+nf/qn7POf/3yvfd/61reyL3/5y8O2xrEi13PRn8svvzxbv379UC9tzBnsuVi6dGn2z//8z9m6deuEyxDJ9Vz853/+Z1ZaWpodOXLkXCxvTMn1XPzLv/xLNnPmzF77HnzwwWzatGnDtsax6GzCZageu0f8qaJjx47Fnj17oqamptf+mpqa2LVrV7/HvPrqq33mv/71r8fu3bvj448/Hra1jnaDORd/6sSJE3H06NEh/U2gY9Fgz8Vjjz0Wb775Zqxbt264lzhmDOZcPP/881FVVRX3339/XHzxxXHZZZfF6tWr46OPPjoXSx61BnMuqqur4/Dhw7F9+/bIsizeeeedePrpp+Paa689F0vm/xmqx+5B/XboodTe3h7d3d19fkljWVlZn1/OeEpra2u/88ePH4/29vYoLy8ftvWOZoM5F3/qBz/4QXzwwQdxww03DMcSx4zBnIvf/e53cffdd0djY2MUFIz4t/aoMZhzceDAgXj55ZejuLg4nn322Whvb4/bb7893n33Xa9z+QQGcy6qq6tjy5YtsXTp0vjjH/8Yx48fj2984xvxox/96Fwsmf9nqB67R/yKyyl5eXm9bmdZ1mffn5vvbz+5y/VcnPLkk0/G9773vdi6dWtceOGFw7W8MeVsz0V3d3fceOONsX79+rjsssvO1fLGlFy+L06cOBF5eXmxZcuWmDt3bixevDgeeOCBePzxx111GQK5nIt9+/bFihUr4p577ok9e/bECy+8EAcPHvRrZ0bIUDx2j/j/lk2ZMiXy8/P71HJbW1ufMjvloosu6ne+oKAgJk+ePGxrHe0Gcy5O2bp1a9x6663x1FNPxdVXXz2cyxwTcj0XR48ejd27d0dTU1N85zvfiYiTD55ZlkVBQUHs2LEjrrrqqnOy9tFmMN8X5eXlcfHFF0dpaWnPvlmzZkWWZXH48OG49NJLh3XNo9VgzkV9fX0sWLAg7rzzzoiI+OIXvxiTJk2KhQsXxn333ecK/Tk0VI/dI37FpbCwMCorK6OhoaHX/oaGhqiuru73mPnz5/eZ37FjR1RVVcX48eOHba2j3WDORcTJKy0333xzPPHEE543HiK5nouSkpL4zW9+E3v37u3Zamtr43Of+1zs3bs35s2bd66WPuoM5vtiwYIF8fbbb8f777/fs++NN96IcePGxbRp04Z1vaPZYM7Fhx9+GOPG9X6oy8/Pj4jT/7fPuTFkj905vZR3mJz68bZNmzZl+/bty1auXJlNmjQp+/3vf59lWZbdfffd2U033dQzf+pHqlatWpXt27cv27Rpkx+HHiK5nosnnngiKygoyB5++OGspaWlZ3vvvfdG6ksYNXI9F3/KTxUNnVzPxdGjR7Np06Zl119/ffb6669nO3fuzC699NLstttuG6kvYdTI9Vw89thjWUFBQbZhw4bszTffzF5++eWsqqoqmzt37kh9CaPG0aNHs6ampqypqSmLiOyBBx7Impqaen40fbgeu8+LcMmyLHv44YezioqKrLCwMJszZ062c+fOnv+2fPny7Morr+w1/6tf/Sr767/+66ywsDD7zGc+k23cuPEcr3j0yuVcXHnllVlE9NmWL19+7hc+CuX6ffH/CZehleu52L9/f3b11VdnEyZMyKZNm5bV1dVlH3744Tle9eiU67l48MEHs8svvzybMGFCVl5env3d3/1ddvjw4XO86tHnxRdfPOP9/3A9dudlmWtlAEAaRvw1LgAAZ0u4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMv4PC+AHXtk5u8sAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    " \n",
    "\n",
    "#b) Add a horizontal line at y = 0.5 using a dashed line style and label it as 'y = 0.5'.\n",
    "\n",
    "plt.axhline(y=0.5,color='red',linestyle='--' ,label='y=0.5')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0d96f8bb-0f55-4732-92a8-2037caf0a8ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.lines.Line2D at 0x7ff7d4b5ebf0>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    " \n",
    "# c) Add a vertical line at x = 0.5 using a dotted line style and label it as 'x = 0.5'.\n",
    "plt.axvline(x=0.5,linestyle=':',color='blue',label='x=0.5')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5a738018-8f27-46ad-b447-4f171a689566",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'y-axis')"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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VVWV95adna1LL71UVVVVGjduXLBGDzln83dj/Pjx+vrrr3XkyBHv2ueff67w8HANGjQooPOGsrM5FseOHVN4ePuXzoiICEn/fzYCweG312+f3lrdDZz6VcjVq1dbu3fvtnJycqxevXpZX331lWVZljV//nwrKyvLu/2pX7+bO3eutXv3bmv16tX8+ryf+HosXnnlFSsyMtJ65plnLLfb7b0dPnzYrqcQUnw9Hv+L3xrzH1+PRVNTkzVo0CDrrrvusj799FNr8+bNVnJysnXvvffa9RRChq/H4oUXXrAiIyOtgoIC68svv7S2bt1qpaamWmPHjrXrKYSMpqYmq7Ky0qqsrLQkWcuWLbMqKyu9H2UQqNfvkAshy7KsZ555xkpMTLSioqKsMWPGWJs3b/b+2fTp063rr7++3fabNm2yrr76aisqKsoaOnSoVVhYGOSJQ5cvx+L666+3JHW4TZ8+PfiDhyhf/278N0LIv3w9Fnv27LFuvvlmq2fPntagQYOs3Nxc69ixY0GeOjT5eixWrFhhXX755VbPnj2thIQE6xe/+IV14MCBIE8dev71r3/94GtAoF6/wyyLc3kAAMBMIfUeIQAAAF8QQgAAwFiEEAAAMBYhBAAAjEUIAQAAYxFCAADAWIQQAAAwFiEEwEg33HCDcnJy7B4DgM34QEUARjp06JB69OihCy64wO5RANiIEAIAAMbi0hgAW3377bfq37+//vSnP3nXPvjgA0VFRamsrKzTfT766CNNnDhRcXFxcjgcuv766/Xxxx97/3zTpk2KiopSeXm5d+3xxx9XXFyc3G63pI6XxgoKCpScnKyYmBjFx8frrrvu8vMzBdAVEUIAbHXRRRepqKhIixYt0s6dO3XkyBH98pe/1OzZs+V0Ojvdp6mpSdOnT1d5ebnef/99JScna/LkyWpqapL0/5GTlZUlj8ejXbt2KS8vT88995wSEhI63N/OnTs1Z84cLVmyRJ999pk2btyo6667LqDPG0DXwKUxAF3C/fffr7///e+65pprtGvXLn300UeKiYk5o31bW1t14YUX6pVXXtGtt94qSWppadG1116r5ORkffrpp0pLS9Nzzz3n3eeGG27Q6NGjtXz5cq1fv14zZ87UgQMHeM8QYBjOCAHoEv7yl7/oxIkTev3111VcXKyYmBhVV1fr/PPP995OXT6rq6tTdna2hg8fLofDIYfDoSNHjqi6utp7f1FRUfrrX/+qdevW6fvvv9fy5ctP+9gTJ05UYmKihg0bpqysLBUXF+vYsWOBfsoAuoBIuwcAAEnau3evvv76a7W1tWn//v0aNWqUBgwYoKqqKu82ffr0kSTNmDFD3377rZYvX67ExERFR0crLS1NLS0t7e5z+/btkk7+htihQ4fUq1evTh/7ggsu0Mcff6xNmzaprKxMjzzyiBYtWqSPPvpIvXv3DsjzBdA1cGkMgO1aWlo0duxYjR49WpdddpmWLVumTz75RPHx8Z1uf8EFF6igoEBZWVmSpJqaGg0ZMkRPPPGE9w3QX375pUaPHq0VK1bo9ddf13/+8x/94x//UHj4yRPh/31p7H8dPXpUvXv3VklJie64446APGcAXQNnhADYLi8vTx6PRytWrND555+vd999V7NmzdLbb7/d6faXXHKJXn75ZaWmpqqxsVHz5s1Tz549vX/e2tqqrKwsOZ1OzZw5UxkZGbryyiv1+OOPa968eR3u7+2339bevXt13XXX6cILL1Rpaana2tp06aWXBuw5A+gaeI8QAFtt2rRJy5cv18svv6zY2FiFh4fr5Zdf1tatW1VYWNjpPkVFRfruu+909dVXKysrS3PmzFG/fv28f/7HP/5RX331lZ599llJUv/+/fX888/rD3/4Q7tLbaf07t1b69ev10033aQRI0Zo5cqVevXVV3XFFVcE5DkD6Dq4NAYAAIzFGSEAAGAsQggAABiLEAIAAMYihAAAgLEIIQAAYCxCCAAAGIsQAgAAxiKEAACAsQghAABgLEIIAAAYixACAADGIoQAAICx/g/ThChuUA60tAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "#d) Label the x-axis as 'X-axis' and the y-axis as 'Y-axis'.\n",
    "plt.xlabel('x-axis')\n",
    "plt.ylabel('y-axis')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7f46a80d-a916-4278-bfad-596322af5108",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Advanced Scatter Plot of Random Values')"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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NG+88YYpKCiosu/WrVtNo0aNTLt27cz8+fPNu+++a1555RUzfPhwU1xcbIwx5quvvjL//Oc/zWuvvWbef/99s3LlSjN27Fjj5eVl1q1bZ4wx5s8//zRr1qwxkszYsWNNTk6OycnJMd99953ZtWuXuf32240ks2zZMudrRUVFxhhj/ud//sc4HA5z4403mpUrV5ply5aZXr16meDgYPPll1+6rBNfX1/Trl07k5aWZt59912zdu3aKpdtwYIFRpLZtGmTS/tTTz1lJJnnnnvOGGPMunXrjCTnshhjzKJFi4wkk5SUZJYvX24yMzNNTEyM8fPzM9nZ2cYYc9zlqkx15vvdd9+ZOXPmGEnm4YcfNjk5OS7r4e8q6l+yZIlL+8qVK40k8+STT7q0jx492qSnp5usrCyTlZVlHnzwQRMYGGhSU1Nd+kVFRZnWrVubrl27mpdeesmsXbvWXH311UaSWb9+vbNfdb+fxhhz8803G0nmtttuM2vWrDHz5883zZo1M23atDE///yzs1/F965Tp04mPT3drF271gwZMsRIMqmpqeacc84xixcvNqtWrTI9e/Y0/v7+5qeffqpyHRlz9PsXFRVlzj//fJf2srIy06JFC9OzZ0+P11FiYqJJTEx0G4u/fpaMMWbnzp1GklmwYIGz7b333jN+fn4mISHBZGZmmjVr1pjRo0e79Rs3bpwJCgoys2bNMuvWrTMrV640jzzyiHn66aePubw4uQguDcRLL71kJJn58+cbY4w5ePCgadSokUlISHDpl5ycbAIDA83evXudbWVlZaZz584ufxhLS0tNRESEGTFihMv0d911l/Hz86tyA15eXm5KS0vNSy+9ZLy9vc0vv/zifC0xMdFIMh9//LHLNF27djUDBgxwPp85c2aloemvFi9ebCSZpUuXurRv2rTJSDJz5841xvxf0Jo4caJLv4qN3vGCS0U9fn5+RpKRZKKjo01KSor57LPPXPr17dvXNG7c2Ozfv/+486xQVlZmSktLTb9+/cw//vEPZ/vPP/9sJJkZM2a4TfP444+7bcSMMSYvL8/4+PiY22+/3aX94MGDJjIy0gwfPtzZNmrUKCPJZGRkVKvOiuDy0UcfmdLSUnPw4EGzcuVK06xZM3PGGWc4P09/39iUl5ebli1bmnPOOceUl5e71NS8eXMTHx9/3OWqjCfzrSqMVKaib2ZmpiktLTWHDh0yGzZsMJ06dTJdu3Y1v/766zFrKi0tNTNnzjTh4eHmyJEjzteioqJMQECA+fHHH51tf/zxhwkLCzPjxo1ztlX3+1nxub7llltcavj444+NJHPPPfc42yq+d5s3b3a2FRYWGm9vbxMYGOgSUrZu3er2j0lVZsyYYSSZTz/91Nn21ltvGUnm+eef93gdnUhw6dy5s7ngggtMaWmpS98hQ4aYFi1aOD8j3bp1M8OGDTvusuHU4lBRA5Genq7AwEBdc801kqRGjRrp6quvVnZ2tssJhevWrVO/fv0UERHhbPP29lZycrLL/Hx8fHT99ddr2bJlKioqkiSVl5fr5Zdf1hVXXOFyXDs3N1eXX365wsPD5e3tLV9fX40cOVLl5eX65ptvXOYbGRmpHj16uLSde+65LocaVq9erY4dO6p///5VLu/KlSvVuHFjDR06VGVlZc7H+eefr8jISOfu5XXr1kmS2/kXw4cPl49P9U4Bu++++5SXl6eMjAyNGzdOjRo10vz58xUTE+PcxXzo0CGtX79ew4cPdx7mqcr8+fPVvXt3BQQEyMfHR76+vnr33Xe1ffv2atVTlbVr16qsrEwjR450WScBAQFKTEys9LDLlVde6dF79OzZU76+vjrjjDM0ZMgQRUZGavXq1S6fp7/6+uuvtWfPHt1www0uh9UaNWqkK6+8Uh999FGlhzOPp67mWyE5OVm+vr4KCgpS7969VVxcrLfffluNGzd26ffee++pf//+Cg0NdX7277//fhUWFmr//v0ufc8//3y1bdvW+TwgIEAdO3Z0+exX9/tZ8bn++1VxPXr0UJcuXfTuu++6tLdo0UIxMTHO52FhYWrevLnOP/98tWzZ0tnepUsXScc/9CdJY8aMkZeXl8vhrgULFig4ONilXk/WUU189913+uqrr5zf8b9+9gcNGqT8/Hx9/fXXko6un9WrV2vq1Kl6//339ccff5zw+6P2EVwagO+++04ffPCBBg8eLGOMDhw4oAMHDuiqq66SJJc/LIWFhYqMjHSbR2VtN954o/7880+99tprko5uGPPz8zVmzBhnn7y8PCUkJOinn37SU089pezsbG3atElz5syRJLc/DH8/kU+S/P39Xfr9/PPPat269TGXed++fTpw4ID8/Pzk6+vr8ti7d68KCgqcy1vZ8vn4+FRaS1UiIiI0ZswYzZ8/X59//rnWr18vPz8/jR8/XpL066+/qry8/Lh1z5o1S//85z8VFxenpUuX6qOPPtKmTZt02WWXnfAf0YrzLy688EK3dZKZmelcJxWCgoIUEhLi0Xu89NJL2rRpk3Jzc7Vnzx59/vnn6t27d5X9j3WOUMuWLXXkyBH9+uuvHtVQl/Ot8Oijj2rTpk1av369pk+frn379mnYsGHOc5Uk6ZNPPlFSUpKko5f/btiwQZs2bdL06dMl1eyzX93v5/GWv+L1CmFhYW79/Pz83Nr9/PwkSX/++adb/7+LiopSv3799Oqrr6qkpEQFBQVauXKlrr76ap1xxhmSPF9HNVHxuZ88ebLb5/6WW26RJOdnf/bs2br77ru1fPly9enTR2FhYRo2bBhXi51muKqoAcjIyJAxRq+//rpef/11t9dffPFFPfTQQ/L29lZ4eLj27t3r1qeytq5du6pHjx5asGCBxo0bpwULFqhly5bOP0SStHz5cv3+++9atmyZoqKinO0ncplws2bN3E4w/LumTZsqPDy8yhMJK/5wVmws9u7dq1atWjlfLysrc/vj7omLL75YSUlJWr58ufbv36+wsDB5e3sft+5XXnlFl1xyiebNm+fSfvDgwRrXUqFp06aSpNdff91lLKricDg8fo8uXbo4T1Stjor1n5+f7/banj175OXlpSZNmnhcR13Nt0L79u2dy3nxxRcrMDBQ9957r55++mlNnjxZkvTaa6/J19dXK1euVEBAgHPa5cuX1/h9q/v9/Ovy/z0s79mzx/lZqGtjx45VVlaW3nzzTe3Zs0eHDx/W2LFjna+fyDqq6P/XsCjJLYBXLOu0adP0X//1X5XOq1OnTpKk4OBgpaamKjU1Vfv27XPufRk6dKjLif84tdjjUs+Vl5frxRdf1Jlnnql169a5Pe68807l5+dr9erVko5ewvruu++6XB1RXl6uzMzMSuc/ZswYffzxx/rwww/11ltvadSoUfL29na+XrHx8/f3d7YZY/T888/XeJkGDhyob775Ru+9916VfYYMGaLCwkKVl5crNjbW7VHxh6riCpJFixa5TP/vf/9bZWVlx61l3759lV5ZVV5erm+//VZBQUFq3LixAgMDlZiYqCVLlrj9Yf0rh8Phsq4k6fPPP3e5Ekb6v/VZ2X+kVb02YMAA+fj46Pvvv690nXgSOGpLp06d1KpVK7366qsuV5H8/vvvWrp0qfOKIOnYy3wi860Nd911l8466yw98sgjzpBZcSO+v34f/vjjD7388ss1fp/qfj/79u0r6WgQ/qtNmzZp+/btNbpCrCaGDRum8PBwZWRkaMGCBerYsaPzKi7pxNZRu3btJMntJo8rVqxwed6pUyd16NBBn332WZWf+4p/ZP4qIiJCo0eP1rXXXquvv/76hA4tonaxx6WeW716tfbs2aNHH3200ss8u3XrpmeeeUbp6ekaMmSI7r33Xq1YsUJ9+/bV/fffr6CgIM2ZM6fKG4hde+21mjRpkq699lqVlJS4HVO/9NJL5efnp2uvvVZ33XWX/vzzT82bN++EdtNPmDBBmZmZuuKKKzR16lT16NFDf/zxh9avX68hQ4aoT58+uuaaa7Ro0SINGjRI48ePV48ePeTr66vdu3dr3bp1uuKKK/SPf/xDXbp00fXXX69//etf8vX1Vf/+/fX//t//0xNPPFGtwyQvv/yynn32WY0YMUIXXnihQkNDtXv3br3wwgv68ssvdf/99zt3r8+aNUsXXXSR4uLiNHXqVJ111lnat2+fVqxYoWeffdZ5XsiDDz6oGTNmKDExUV9//bVmzpyp6OholyB1xhlnKCoqSm+++ab69eunsLAwNW3aVO3atdM555wj6egdTEeNGiVfX1916tRJ7dq108yZMzV9+nTt2LFDl112mZo0aaJ9+/bpk08+cf63eTJ5eXnpscce03XXXachQ4Zo3LhxKikp0eOPP64DBw7okUcecfatarkq2+h4Mt/a4Ovrq4cffljDhw/XU089pXvvvVeDBw/WrFmzNGLECN18880qLCzUE0884RZMPVHd72enTp1088036+mnn5aXl5cGDhyoH374Qffdd5/atGmjiRMnnugiV4u/v7+uu+46Pf300zLGuK33E1lHkZGR6t+/v9LS0tSkSRNFRUXp3XffrfRuvM8++6wGDhyoAQMGaPTo0WrVqpV++eUXbd++XZ9++qmWLFki6eitHIYMGaJzzz1XTZo00fbt2/Xyyy/XetDFCTqVZwaj7g0bNsz4+fkd80qWa665xvj4+DivVNiwYYPzssfIyEgzZcoU89xzz1V5RceIESOMJNO7d+9K5//WW2+Z8847zwQEBJhWrVqZKVOmmNWrV7tdEZCYmGjOPvtst+lHjRploqKiXNp+/fVXM378eNO2bVvj6+trmjdvbgYPHmy++uorZ5/S0lLzxBNPON+7UaNGpnPnzmbcuHHm22+/dfYrKSkxd955p2nevLkJCAgwPXv2NDk5OSYqKuq4VxVt27bN3HnnnSY2NtY0a9bM+Pj4mCZNmpjExETz8ssvV9r/6quvNuHh4cbPz8+0bdvWjB492vz555/OWiZPnmxatWplAgICTPfu3c3y5csrXQf/+c9/zAUXXGD8/f3droCaNm2aadmypfHy8nJbz8uXLzd9+vQxISEhxt/f30RFRZmrrrrK/Oc//3FZ58HBwcdc9r+q6nLov6vqSpDly5ebuLg4ExAQYIKDg02/fv3Mhg0b3KY/1nJVpjrzrclVRVX1jYuLM02aNDEHDhwwxhiTkZFhOnXqZPz9/U379u1NWlqaSU9Pd/suRUVFmcGDB7vN7+9X0hhT/e9neXm5efTRR03Hjh2Nr6+vadq0qbn++uvNrl273N6jsu9dVTVJMrfeemtVq8jNZ599ZiQZb29vs2fPHrfXq7uOKlsX+fn55qqrrjJhYWEmNDTUXH/99Wbz5s1uVxVV1DF8+HDTvHlz4+vrayIjI03fvn2dV1oaY8zUqVNNbGysadKkibOeiRMnHvM2Bzj5HMYc5y4/AAAApwnOcQEAANYguAAAAGsQXAAAgDU8Di4ffPCBhg4dqpYtW8rhcFTrevv169crJiZGAQEBat++vebPn1+TWgEAQAPncXD5/fffdd555+mZZ56pVv+dO3dq0KBBSkhIUG5uru655x7dcccdWrp0qcfFAgCAhu2EripyOBx64403NGzYsCr73H333VqxYoXL76ykpKTos88+c7upFgAAwLHU+Q3ocnJyXG4BLx29g2d6erpKS0vl6+vrNk1JSYnLbZyPHDmiX375ReHh4TW6DTkAADj5jDE6ePCgWrZs6fKDpyeizoPL3r173X4ZNiIiQmVlZSooKKj0R8DS0tJO+h08AQBA3di1a9dxf2S2uk7KLf//vpek4uhUVXtPpk2bpkmTJjmfFxUVqW3bttq1a5fHv1YLAABOjeLiYrVp06bSn+aoqToPLpGRkW6/XLp//375+PhU+jPu0tHft6jstypCQkIILgAAWKY2T/Oo8/u49OrVS1lZWS5t77zzjmJjYys9vwUAAKAqHgeX3377TVu3btXWrVslHb3ceevWrcrLy5N09DDPyJEjnf1TUlL0448/atKkSdq+fbsyMjKUnp6uyZMn184SAACABsPjQ0WbN29Wnz59nM8rzkUZNWqUFi5cqPz8fGeIkaTo6GitWrVKEydO1Jw5c9SyZUvNnj1bV155ZS2UDwAAGhIrfh26uLhYoaGhKioq4hwXAAAsURfbb36rCAAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGCNGgWXuXPnKjo6WgEBAYqJiVF2dvYx+y9atEjnnXeegoKC1KJFC40ZM0aFhYU1KhgAADRcHgeXzMxMTZgwQdOnT1dubq4SEhI0cOBA5eXlVdr/ww8/1MiRIzV27Fh9+eWXWrJkiTZt2qSbbrrphIsHAAANi8fBZdasWRo7dqxuuukmdenSRf/617/Upk0bzZs3r9L+H330kdq1a6c77rhD0dHRuuiiizRu3Dht3rz5hIsHAAANi0fB5fDhw9qyZYuSkpJc2pOSkrRx48ZKp4mPj9fu3bu1atUqGWO0b98+vf766xo8eHCV71NSUqLi4mKXBwAAgEfBpaCgQOXl5YqIiHBpj4iI0N69eyudJj4+XosWLVJycrL8/PwUGRmpxo0b6+mnn67yfdLS0hQaGup8tGnTxpMyAQBAPVWjk3MdDofLc2OMW1uFbdu26Y477tD999+vLVu2aM2aNdq5c6dSUlKqnP+0adNUVFTkfOzatasmZQIAgHrGx5POTZs2lbe3t9velf3797vthamQlpam3r17a8qUKZKkc889V8HBwUpISNBDDz2kFi1auE3j7+8vf39/T0oDAAANgEd7XPz8/BQTE6OsrCyX9qysLMXHx1c6zaFDh+Tl5fo23t7eko7uqQEAAKgujw8VTZo0SS+88IIyMjK0fft2TZw4UXl5ec5DP9OmTdPIkSOd/YcOHaply5Zp3rx52rFjhzZs2KA77rhDPXr0UMuWLWtvSQAAQL3n0aEiSUpOTlZhYaFmzpyp/Px8devWTatWrVJUVJQkKT8/3+WeLqNHj9bBgwf1zDPP6M4771Tjxo3Vt29fPfroo7W3FAAAoEFwGAuO1xQXFys0NFRFRUUKCQk51eUAAIBqqIvtN79VBAAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALBGjYLL3LlzFR0drYCAAMXExCg7O/uY/UtKSjR9+nRFRUXJ399fZ555pjIyMmpUMAAAaLh8PJ0gMzNTEyZM0Ny5c9W7d289++yzGjhwoLZt26a2bdtWOs3w4cO1b98+paen66yzztL+/ftVVlZ2wsUDAICGxWGMMZ5MEBcXp+7du2vevHnOti5dumjYsGFKS0tz679mzRpdc8012rFjh8LCwmpUZHFxsUJDQ1VUVKSQkJAazQMAAJxcdbH99uhQ0eHDh7VlyxYlJSW5tCclJWnjxo2VTrNixQrFxsbqscceU6tWrdSxY0dNnjxZf/zxR5XvU1JSouLiYpcHAACAR4eKCgoKVF5eroiICJf2iIgI7d27t9JpduzYoQ8//FABAQF64403VFBQoFtuuUW//PJLlee5pKWlKTU11ZPSAABAA1Cjk3MdDofLc2OMW1uFI0eOyOFwaNGiRerRo4cGDRqkWbNmaeHChVXudZk2bZqKioqcj127dtWkTAAAUM94tMeladOm8vb2dtu7sn//fre9MBVatGihVq1aKTQ01NnWpUsXGWO0e/dudejQwW0af39/+fv7e1IaAABoADza4+Ln56eYmBhlZWW5tGdlZSk+Pr7SaXr37q09e/bot99+c7Z988038vLyUuvWrWtQMgAAaKg8PlQ0adIkvfDCC8rIyND27ds1ceJE5eXlKSUlRdLRwzwjR4509h8xYoTCw8M1ZswYbdu2TR988IGmTJmiG2+8UYGBgbW3JAAAoN7z+D4uycnJKiws1MyZM5Wfn69u3bpp1apVioqKkiTl5+crLy/P2b9Ro0bKysrS7bffrtjYWIWHh2v48OF66KGHam8pAABAg+DxfVxOBe7jAgCAfU75fVwAAABOJYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDVqFFzmzp2r6OhoBQQEKCYmRtnZ2dWabsOGDfLx8dH5559fk7cFAAANnMfBJTMzUxMmTND06dOVm5urhIQEDRw4UHl5ececrqioSCNHjlS/fv1qXCwAAGjYHMYY48kEcXFx6t69u+bNm+ds69Kli4YNG6a0tLQqp7vmmmvUoUMHeXt7a/ny5dq6dWuVfUtKSlRSUuJ8XlxcrDZt2qioqEghISGelAsAAE6R4uJihYaG1ur226M9LocPH9aWLVuUlJTk0p6UlKSNGzdWOd2CBQv0/fffa8aMGdV6n7S0NIWGhjofbdq08aRMAABQT3kUXAoKClReXq6IiAiX9oiICO3du7fSab799ltNnTpVixYtko+PT7XeZ9q0aSoqKnI+du3a5UmZAACgnqpekvgbh8Ph8twY49YmSeXl5RoxYoRSU1PVsWPHas/f399f/v7+NSkNAADUYx4Fl6ZNm8rb29tt78r+/fvd9sJI0sGDB7V582bl5ubqtttukyQdOXJExhj5+PjonXfeUd++fU+gfAAA0JB4dKjIz89PMTExysrKcmnPyspSfHy8W/+QkBB98cUX2rp1q/ORkpKiTp06aevWrYqLizux6gEAQIPi8aGiSZMm6YYbblBsbKx69eql5557Tnl5eUpJSZF09PyUn376SS+99JK8vLzUrVs3l+mbN2+ugIAAt3YAAIDj8Ti4JCcnq7CwUDNnzlR+fr66deumVatWKSoqSpKUn59/3Hu6AAAA1ITH93E5FeriOnAAAFC3Tvl9XAAAAE4lggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANWoUXObOnavo6GgFBAQoJiZG2dnZVfZdtmyZLr30UjVr1kwhISHq1auX1q5dW+OCAQBAw+VxcMnMzNSECRM0ffp05ebmKiEhQQMHDlReXl6l/T/44ANdeumlWrVqlbZs2aI+ffpo6NChys3NPeHiAQBAw+IwxhhPJoiLi1P37t01b948Z1uXLl00bNgwpaWlVWseZ599tpKTk3X//fdX+npJSYlKSkqcz4uLi9WmTRsVFRUpJCTEk3IBAMApUlxcrNDQ0Frdfnu0x+Xw4cPasmWLkpKSXNqTkpK0cePGas3jyJEjOnjwoMLCwqrsk5aWptDQUOejTZs2npQJAADqKY+CS0FBgcrLyxUREeHSHhERob1791ZrHk8++aR+//13DR8+vMo+06ZNU1FRkfOxa9cuT8oEAAD1lE9NJnI4HC7PjTFubZVZvHixHnjgAb355ptq3rx5lf38/f3l7+9fk9IAAEA95lFwadq0qby9vd32ruzfv99tL8zfZWZmauzYsVqyZIn69+/veaUAAKDB8+hQkZ+fn2JiYpSVleXSnpWVpfj4+CqnW7x4sUaPHq1XX31VgwcPrlmlAACgwfP4UNGkSZN0ww03KDY2Vr169dJzzz2nvLw8paSkSDp6fspPP/2kl156SdLR0DJy5Eg99dRT6tmzp3NvTWBgoEJDQ2txUQAAQH3ncXBJTk5WYWGhZs6cqfz8fHXr1k2rVq1SVFSUJCk/P9/lni7PPvusysrKdOutt+rWW291to8aNUoLFy488SUAAAANhsf3cTkV6uI6cAAAULdO+X1cAAAATiWCCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABr1Ci4zJ07V9HR0QoICFBMTIyys7OP2X/9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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    " \n",
    "\n",
    "#e) Set the title of the \u0018lot as 'Advanced Scatter Plot of Random Values'.\n",
    "plt.title('Advanced Scatter Plot of Random Values')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "98141ddc-96fa-42d7-a461-e7000233535a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.\n"
     ]
    },
    {
     "data": {
      "image/png": "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D/kcPT090dPT03+/q6srLrvssjh69GiUlJTkslwAYJx0d3dHRUVFvPXWW1FaWjoyD5rloKenJ8vPz8927do1YHzt2rXZZz7zmSGPqampydauXTtgbNeuXVlBQUHW29s75DGbNm3KIsLNzc3Nzc1tAtxee+21XHLjfRVEDjo7O6Ovry/KysoGjJeVlUV7e/uQx7S3tw85/9SpU9HZ2Rnl5eWDjtmwYUPU19f333/rrbdi3rx50draOnLFxrCcqWdnv8afvbhw2IsLi/24cJx5x+Tiiy8escfMKVzOyMvLG3A/y7JBYx80f6jxM4qKiqKoqGjQeGlpqf8RXiBKSkrsxQXCXlw47MWFxX5cOKZMGbkvMef0SLNmzYr8/PxBZ1c6OjoGnVU5Y/bs2UPOLygoiJkzZ+a4XABgMsspXAoLC6OysjKampoGjDc1NUV1dfWQxyxfvnzQ/N27d0dVVVVMnTo1x+UCAJNZzudu6uvr45FHHont27fHoUOHYv369dHa2hp1dXUR8d7nU9asWdM/v66uLl5//fWor6+PQ4cOxfbt22Pbtm1xxx13nPNzFhUVxaZNm4Z8+4ixZS8uHPbiwmEvLiz248IxGnuR89ehI967AN39998fbW1tsXjx4vjBD34Qn/nMZyIi4uabb44//OEP8Zvf/KZ//p49e2L9+vXxyiuvxJw5c+Kuu+7qDx0AgHM1rHABABgP/lYRAJAM4QIAJEO4AADJEC4AQDIumHDZsmVLzJ8/P4qLi6OysjKam5vfd/6ePXuisrIyiouLY8GCBfHwww+P0Uonvlz2YteuXXH11VfHhz70oSgpKYnly5fHr371qzFc7cSW6+/FGS+99FIUFBTEpz71qdFd4CSS61709PTExo0bY968eVFUVBQf+chHYvv27WO02okt173YsWNHXHHFFTF9+vQoLy+PW265JY4fPz5Gq524Xnjhhbjuuutizpw5kZeXF88+++wHHjMir90j9lePzsN//Md/ZFOnTs1+9rOfZQcPHsxuv/327KKLLspef/31IecfPnw4mz59enb77bdnBw8ezH72s59lU6dOzZ566qkxXvnEk+te3H777dl3v/vd7L//+7+zV199NduwYUM2derU7H//93/HeOUTT657ccZbb72VLViwIKutrc2uuOKKsVnsBDecvfjiF7+YLVu2LGtqasqOHDmS/dd//Vf20ksvjeGqJ6Zc96K5uTmbMmVK9sMf/jA7fPhw1tzcnH3iE5/IVq1aNcYrn3gaGxuzjRs3Zk8//XQWEdkzzzzzvvNH6rX7ggiXpUuXZnV1dQPGPvaxj2V33333kPP/9V//NfvYxz42YOxrX/ta9ulPf3rU1jhZ5LoXQ/n4xz+ebd68eaSXNukMdy9Wr16d/du//Vu2adMm4TJCct2LX/7yl1lpaWl2/PjxsVjepJLrXnzve9/LFixYMGDswQcfzObOnTtqa5yMziVcRuq1e9zfKurt7Y39+/dHbW3tgPHa2trYu3fvkMe8/PLLg+Z/4QtfiH379sW77747amud6IazF3/r9OnTceLEiRH9S6CT0XD34tFHH43XXnstNm3aNNpLnDSGsxfPPfdcVFVVxf333x+XXnppXH755XHHHXfEX/7yl7FY8oQ1nL2orq6OY8eORWNjY2RZFm+88UY89dRTce21147FkvkrI/XaPay/Dj2SOjs7o6+vb9AfaSwrKxv0xxnPaG9vH3L+qVOnorOzM8rLy0dtvRPZcPbib33/+9+Pd955J66//vrRWOKkMZy9+P3vfx933313NDc3R0HBuP9qTxjD2YvDhw/Hiy++GMXFxfHMM89EZ2dnfP3rX48333zT51zOw3D2orq6Onbs2BGrV6+O//u//4tTp07FF7/4xfjRj340Fkvmr4zUa/e4n3E5Iy8vb8D9LMsGjX3Q/KHGyV2ue3HGE088Ed/5zndi586dcckll4zW8iaVc92Lvr6+uOGGG2Lz5s1x+eWXj9XyJpVcfi9Onz4deXl5sWPHjli6dGlcc8018cADD8Rjjz3mrMsIyGUvDh48GGvXro177rkn9u/fH88//3wcOXLEn50ZJyPx2j3u/1k2a9asyM/PH1TLHR0dg8rsjNmzZw85v6CgIGbOnDlqa53ohrMXZ+zcuTNuvfXWePLJJ+Oqq64azWVOCrnuxYkTJ2Lfvn3R0tIS3/zmNyPivRfPLMuioKAgdu/eHVdeeeWYrH2iGc7vRXl5eVx66aVRWlraP7Zo0aLIsiyOHTsWCxcuHNU1T1TD2YuGhoZYsWJF3HnnnRER8clPfjIuuuiiqKmpifvuu88Z+jE0Uq/d437GpbCwMCorK6OpqWnAeFNTU1RXVw95zPLlywfN3717d1RVVcXUqVNHba0T3XD2IuK9My0333xzPP744943HiG57kVJSUn87ne/iwMHDvTf6urq4qMf/WgcOHAgli1bNlZLn3CG83uxYsWK+NOf/hRvv/12/9irr74aU6ZMiblz547qeiey4ezFyZMnY8qUgS91+fn5EfH//2ufsTFir905fZR3lJz5etu2bduygwcPZuvWrcsuuuii7A9/+EOWZVl29913ZzfeeGP//DNfqVq/fn128ODBbNu2bb4OPUJy3YvHH388KygoyB566KGsra2t//bWW2+N148wYeS6F3/Lt4pGTq57ceLEiWzu3LnZl7/85eyVV17J9uzZky1cuDC77bbbxutHmDBy3YtHH300KygoyLZs2ZK99tpr2YsvvphVVVVlS5cuHa8fYcI4ceJE1tLSkrW0tGQRkT3wwANZS0tL/1fTR+u1+4IIlyzLsoceeiibN29eVlhYmC1ZsiTbs2dP/7/ddNNN2Wc/+9kB83/zm99k//iP/5gVFhZmH/7wh7OtW7eO8Yonrlz24rOf/WwWEYNuN91009gvfALK9ffirwmXkZXrXhw6dCi76qqrsmnTpmVz587N6uvrs5MnT47xqiemXPfiwQcfzD7+8Y9n06ZNy8rLy7OvfvWr2bFjx8Z41RPPr3/96/f9///Reu3OyzLnygCANIz7Z1wAAM6VcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGT8P2368IoO4Ji+AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#f) Dis\u0018lay a legend for the scatter \u0018lot, the horizontal line, and the vertical line.\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7edacea4-98ac-41a5-8f56-d6d65d98506b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Create a time-series dataset\n",
    "dates = pd.date_range('2024-01-01', periods=365)\n",
    "temperature = np.random.normal(25, 5, 365)\n",
    "humidity = np.random.normal(50, 10, 365)\n",
    "\n",
    "data = {'Date': dates, 'Temperature': temperature, 'Humidity': humidity}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "60d3803d-3e7a-45e8-95b8-2ac340a0c8dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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uUYsWbJEVCqVyPtPO+20WX1Bm3T7+ZS88IUvFJdccknitmcT3XheZZC3e/fuOr/t7KEbz6vJN7/5TeE4jnjkkUdqfd1ZRzee3xNOOEG84x3v0P7uLW95izjppJNSfefZQqedW8qf/dmfWYM8Cs+d7LTyvK5cuVJ8+MMfrmt/eE5cH7M+XdNEyslz584FADz88MN46qmncPbZZ6v35HI5nHbaafjFL36RuJ2hoSH4vq9e2759O173utfhi1/8Ivr6+lLtzy9/+UucdtppWrPIc845B08++SQeeeSRer7arKQXzuedd96JX/ziFzjttNNSfcZsoJvP65YtW7B48WKceeaZuOWWW1Jtf7bQzedV8tnPfhZnnXUWVq5cmeozZhPdeH4nJyeRz+e1vysUCvj1r3+NYrGY6nNmA512bpnm0MrzCgDXXnst5s2bh82bN+O9730vpqamEveH58T1wUEeQQiBt7/97Tj55JOxceNGAMBTTz0FAFi4cKH23oULF6rfmezatQvvec978Bd/8Rfati+99FJcdtllOProo1Pv01NPPWX9bLpvjJ1uP5/Lli1DLpfD0UcfjTe+8Y147Wtfm/pzepluPa+LFy/Gddddh69//ev4xje+gQ0bNuDMM8/E//zP/6T+nF6mW88rZdu2bbjpppv4XrXQref3nHPOwWc+8xncfvvtEELgN7/5Da6//noUi0Xs3Lkz9Wf1Mp14bpnp08rzCgBvectb8NWvfhW33HIL3vSmN+EjH/kILr/88sR94jlxffi13zJ7eNOb3oS77roLP//5zyO/cxxH+1kIEXkNAPbu3YvzzjsPhx56KK688kr1+sc+9jHs3bsX73rXu2I//7DDDsOjjz4KADjllFNw0003xX627XVGp9vP589+9jPs27cPv/rVr/DOd74TBx10EC6++OKkrzwr6NbzumHDBmzYsEH9/oQTTsBjjz2Gf/qnf8Kpp56a+J1nA916Xin/9m//hpGREavJw2ynW8/v3/3d3+Gpp57C8ccfDyEEFi5ciEsvvRQf+MAH4Hlemq/e83TquWWmRyvPKwC87W1vU/8+/PDDMWfOHLz4xS9W6h7PiacPB3lV3vzmN+PGG2/E//zP/2DZsmXq9UWLFgEIVggWL16sXt+xY0dkNWFsbAznnnsuBgYG8M1vfhOZTEb97uabb8avfvUrTWIGgKOP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\n",
      "text/plain": [
       "<Figure size 1000x500 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#a. Plot Temperature and Humidity on the same plot with different y-axes\n",
    "#b) Label the x-axis as 'Date'.\n",
    "#c) Set the title of the \u0018lot as 'Tem\u0018erature and Humidity Over Time'.\n",
    "\n",
    "fig, ax1 = plt.subplots(figsize=(10, 5))\n",
    "\n",
    "color = 'tab:blue'\n",
    "ax1.set_xlabel('Date')\n",
    "ax1.set_ylabel('Temperature (°C)', color=color)\n",
    "ax1.plot(df['Date'], df['Temperature'], color=color)\n",
    "ax1.tick_params(axis='y', labelcolor=color)\n",
    "\n",
    "ax2 = ax1.twinx()\n",
    "color = 'tab:green'\n",
    "ax2.set_ylabel('Humidity (%)', color=color)\n",
    "ax2.plot(df['Date'], df['Humidity'], color=color)\n",
    "ax2.tick_params(axis='y', labelcolor=color)\n",
    "\n",
    "plt.title('Temperature and Humidity Over Time')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22cc18cf-064f-4317-8321-fb7c8b618fa1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c20be831-8b1a-4b30-a255-a9e6bc8dc334",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.01488109, -0.27654147, -0.77285838,  0.09636462,  0.85273547,\n",
       "        1.01766689,  0.07181847,  0.57241021, -1.59839256, -0.57356512,\n",
       "       -0.6124622 ,  1.67557065, -0.20063116, -0.50744442, -0.13865408,\n",
       "       -0.20338933,  0.11925271,  0.05461566, -0.37412713, -1.36279385,\n",
       "        2.84371635, -1.53471264, -0.21149473, -0.38649491, -0.46759057,\n",
       "       -0.46175191, -0.6576523 ,  1.65428994, -1.46206223, -0.59753918,\n",
       "        0.07593372,  1.54666987,  0.79074888, -0.87220741, -0.32252083,\n",
       "        0.15804306, -0.23968451,  0.17228849,  0.27798367, -1.09134143,\n",
       "       -0.01218272,  1.70639588, -0.15730861, -1.39835045,  1.49550772,\n",
       "        0.52566395,  0.0264552 , -0.22658038,  0.04151514, -1.55990006,\n",
       "       -0.871629  , -1.07706493,  0.07533223,  0.35258464,  1.20207796,\n",
       "        0.27168345,  1.01393808,  0.86852634,  0.10388518, -1.10056549,\n",
       "        0.70786547,  1.45461028, -0.38505432,  0.18982215,  1.94141033,\n",
       "        0.2255713 ,  0.52750842,  1.09496663, -2.30007113, -0.82252732,\n",
       "       -0.63837001,  0.89651524, -0.18743817, -1.106483  ,  0.55471382,\n",
       "       -0.25290144, -0.76312767,  1.22254969,  1.38636843,  0.54317681,\n",
       "        0.90853129, -0.38074364,  0.67691259,  1.31356243,  1.04915405,\n",
       "        1.74182737,  2.22849697, -1.71225352, -0.74340651,  1.00304256,\n",
       "       -0.04655499,  1.24895541,  1.11914215,  0.32512301,  0.2568009 ,\n",
       "        0.02080929, -0.97747224,  1.57585685, -0.54121577,  1.45825017,\n",
       "       -0.65741695,  0.87025497, -0.22251442, -1.22094292, -0.04718287,\n",
       "        0.09731236, -0.00428649, -0.67468086, -0.68996171,  0.76126372,\n",
       "       -0.42320583, -2.82930668,  0.82299696, -0.79358068,  0.64332402,\n",
       "        0.87023015,  0.69454865, -1.91643153, -1.52694066,  0.25191072,\n",
       "        0.50178683, -0.17478381,  0.21876196, -1.24034781,  0.20698679,\n",
       "        0.25289777, -0.85048491,  0.63974636, -1.77185913,  1.41829567,\n",
       "       -0.09506295, -0.27007673,  0.79768902,  0.88922825,  2.86457928,\n",
       "       -0.56773038, -1.34178662, -0.88840773,  0.09233208,  0.34165933,\n",
       "        0.23303544,  2.01620951, -0.62676258, -0.35294783,  0.92532222,\n",
       "        0.94086862,  2.50246437,  0.97680689,  0.67505043, -1.10564708,\n",
       "       -0.48048067, -0.5117014 , -0.43567418,  0.26830091,  1.0065981 ,\n",
       "        0.62973033,  0.42675656, -0.15307687,  0.4462794 , -0.98898736,\n",
       "       -1.471577  , -0.53101556,  0.78804388,  0.71613258,  0.12844783,\n",
       "       -0.18680926, -0.11183145, -0.82293714, -0.96683811,  0.67232821,\n",
       "        1.39694719, -2.01664247,  1.08289836, -1.21694765,  0.79011249,\n",
       "       -0.66185061, -0.89605546, -1.30748985, -1.4912357 , -0.46707571,\n",
       "       -0.06698448, -0.83397567,  0.35686773, -1.70962339, -0.93611633,\n",
       "        0.01363413,  0.36157128,  0.58856148, -0.1913662 , -0.8413772 ,\n",
       "       -0.85786709, -1.63983872, -0.69696028,  0.30884085, -0.08010898,\n",
       "       -0.02073094, -0.06143454,  2.18021492, -1.19707675, -0.34948267,\n",
       "        0.37693422,  2.77644718, -1.4326413 , -1.61605546,  0.20273606,\n",
       "        0.57788012, -1.7915629 , -0.86271753, -1.52493326,  1.13941207,\n",
       "        1.6419081 , -0.49809152,  0.97507013, -0.7515427 , -0.23929131,\n",
       "        1.03634204,  0.74104772, -0.5117728 ,  0.43827989,  0.38808447,\n",
       "        0.4063145 ,  0.30283058, -0.5777626 ,  0.62055739,  1.76389845,\n",
       "        0.55752646,  0.84479669,  0.66645875, -0.40164376,  1.17767538,\n",
       "        1.88386943,  0.3108033 ,  0.5089473 , -0.84528848,  0.51680297,\n",
       "        0.12313052,  0.13014441,  0.78285256, -2.18098709, -1.00277812,\n",
       "        0.78117216, -0.59230883, -0.84541252, -0.9937245 , -0.53184582,\n",
       "       -1.02220374,  0.20219776,  0.5914625 , -0.30136548, -1.37411391,\n",
       "        0.33157511, -0.74775714, -1.27668429,  1.82546149, -0.96652668,\n",
       "       -0.15238385,  0.07048653,  0.1887377 , -0.86829371, -2.20678288,\n",
       "        0.63788289,  2.40880818, -0.30720046, -0.25072298,  0.68691179,\n",
       "       -0.19037802, -0.04676132,  1.97699667,  0.52817823,  1.53248395,\n",
       "       -2.10389143, -1.80255661, -0.42945465,  0.50342406, -0.57225658,\n",
       "        0.61786379, -1.081969  ,  0.07253867, -1.12233595, -0.09613746,\n",
       "        0.21774123,  0.84399752,  0.5842804 , -0.46611003,  1.40360043,\n",
       "       -1.73567172, -0.81379998, -0.26750038,  1.83994005,  1.5127218 ,\n",
       "        0.3376981 , -0.00457855,  0.5740224 , -0.89725894, -0.93207936,\n",
       "        1.1099537 , -0.32862274,  0.4455326 , -0.04585283, -1.02656246,\n",
       "        1.40235658, -0.27922588,  0.00424799, -0.91334054, -1.0118363 ,\n",
       "       -1.14216206, -0.57676028,  0.10327274, -0.04174326,  1.00196785,\n",
       "       -0.14259227,  0.41124546,  0.58112454, -0.29499986,  0.43500833,\n",
       "       -1.82362668, -0.20824589, -0.34136426,  1.69754993, -2.42116868,\n",
       "       -1.09438202,  1.22772734,  0.44629511, -0.47413945, -0.39497513,\n",
       "       -0.4299833 ,  1.15348621, -0.18286095, -0.94619862, -1.1088047 ,\n",
       "        0.00342817, -0.66718312,  0.43465591,  0.11227877, -1.31587169,\n",
       "       -2.82500422, -0.39845708,  0.19066577,  1.23458274, -1.55039251,\n",
       "        2.04511172,  1.40811959,  1.25063979, -2.46336664,  0.01720597,\n",
       "       -0.91454512,  0.10419047, -0.64621497, -0.77778329, -1.91320833,\n",
       "        1.08328106,  0.45080236, -0.97038607,  1.65269008,  0.49392391,\n",
       "        1.59321432,  0.49858863,  0.33410814,  1.60853314, -0.95388074,\n",
       "       -1.20436816,  0.15586539,  1.58145616,  2.36895972, -0.79322436,\n",
       "       -0.78575941, -1.34124055,  1.19320555, -0.13197597, -0.99770739,\n",
       "       -0.28035462, -0.86358506, -1.68330706, -2.09900408,  0.21817433,\n",
       "       -0.47956432, -0.06767187, -0.10822743, -0.20119272,  0.54821644,\n",
       "       -0.5522721 ,  0.55687549,  0.79935819,  1.0035552 , -0.17928649,\n",
       "       -1.3292211 , -0.32689838, -0.12923199,  0.53038864, -0.25901165,\n",
       "       -1.06080535, -0.76514188, -1.37804691,  0.57083826, -0.35442592,\n",
       "        1.10348731, -0.80100278, -0.7004014 ,  0.48602026,  1.19858232,\n",
       "        0.2166925 ,  0.44420185,  1.44098853, -0.20594766,  1.33660987,\n",
       "        0.26638657,  0.38529719,  1.14030731,  1.93381071,  1.69542155,\n",
       "       -0.05120092, -0.75489895,  0.95179787,  0.69302095, -0.95420529,\n",
       "       -2.31828745, -0.10637141,  0.7798919 , -0.87011407, -0.9518826 ,\n",
       "       -0.12699403, -1.74643208,  0.76059306, -0.64027985,  1.49875973,\n",
       "        1.22300677,  1.55157983, -1.11303303, -1.05945392, -0.93550228,\n",
       "       -0.79547803, -0.74502422,  0.58047899,  0.72360097, -1.06380423,\n",
       "        0.03277054, -2.07611808,  0.48628843,  0.85570523, -1.907099  ,\n",
       "       -0.43138216, -1.37173906, -0.45950786,  1.65313146, -1.40713568,\n",
       "        0.53033025, -0.87820732, -1.72915721, -0.96021015, -0.65667638,\n",
       "        1.58705727, -0.93754915,  2.28610811, -3.29656264,  1.93256952,\n",
       "        0.38654814,  0.14256745,  0.93560074,  0.54836716,  0.40904043,\n",
       "       -0.71293366,  0.49044327, -1.88692401, -1.49274535, -0.88820996,\n",
       "        0.21374833, -1.83367929, -1.56112195,  1.60390308,  0.99880476,\n",
       "       -0.86345764, -0.60024631,  1.61161689,  0.10853336,  0.79335675,\n",
       "       -0.6813291 ,  2.69437222, -0.47574855, -0.12105896, -0.16237999,\n",
       "       -0.10373729, -1.40064853,  0.56449973, -0.57760068,  0.45492542,\n",
       "        1.08622475,  1.36511378,  1.03467689, -0.70336651,  0.49044136,\n",
       "       -0.93965418, -1.15256814, -0.79550789,  0.52292864,  1.02703182,\n",
       "       -1.12116594, -0.7555699 ,  0.70139491,  0.99340669, -0.06911727,\n",
       "        1.23533979,  0.68839348, -0.37663389,  0.77596142,  0.78342987,\n",
       "        0.60124983,  1.28573566,  0.49291784,  0.76732078,  0.66067632,\n",
       "        0.00465087, -2.46113144,  0.09283655,  0.46076625, -0.28768889,\n",
       "        0.72974255, -0.76631239, -1.82712521,  0.73166784,  0.0788966 ,\n",
       "       -0.8380644 ,  0.97132522, -0.08446576,  1.40085766, -0.76000947,\n",
       "        0.84947987,  0.53922804,  0.35817617, -0.54222346,  0.08214908,\n",
       "        0.48317628, -1.63434465,  0.8679955 ,  0.01168835,  0.08049364,\n",
       "        0.40831892, -0.09286741,  0.24341573,  0.15002375, -2.04161401,\n",
       "       -0.07359224,  0.64897315,  0.52708796, -0.53266108, -0.30383962,\n",
       "        1.3858738 , -1.55873127, -0.04635829,  0.90967059,  0.33705154,\n",
       "       -0.90666212,  0.01252893,  0.27170184, -1.20787853, -2.17200413,\n",
       "        0.8197944 , -0.3894579 ,  0.83804261, -0.43228108,  0.15092547,\n",
       "       -1.3850162 ,  0.6848865 ,  1.35417343, -0.83845169, -1.10036036,\n",
       "        0.60637293, -0.79092031, -0.68134393, -0.36897866, -0.95592375,\n",
       "       -0.44475281, -1.94821004, -0.43819428, -0.10678858, -0.61925921,\n",
       "        0.33596464, -0.14868582, -1.31024963, -0.98778599,  0.1212742 ,\n",
       "        0.15904222,  0.34431754,  1.80688076, -1.43014184, -0.2017866 ,\n",
       "       -0.92176936,  1.10768468,  0.98073742,  1.59067819, -1.37067959,\n",
       "       -0.44840518,  0.44849974,  0.55111286,  0.07063547, -0.74851708,\n",
       "       -0.08177662, -0.25200623, -1.38224741, -0.77750939,  0.86419454,\n",
       "       -1.33277409,  0.06113756, -1.83058097,  2.02124508,  0.53866157,\n",
       "       -0.98263169,  0.14554975, -0.17016918,  1.77751753,  0.09049814,\n",
       "       -1.40069116, -1.53533979, -0.32687651, -0.56995832,  2.82405306,\n",
       "        0.01602427, -0.16786655, -0.86314495,  1.75726595, -0.16774275,\n",
       "       -1.13958806, -1.49697111, -0.2432184 , -0.38283211, -0.86141986,\n",
       "       -0.55167255, -1.4312255 , -1.76953864,  0.75544222, -0.35185596,\n",
       "       -0.25521062,  0.73110644, -1.27097969,  0.16817798, -2.80283945,\n",
       "        1.08603929,  0.25007824,  0.34829177,  0.458158  ,  0.29505337,\n",
       "        0.96241101,  0.05318051, -2.07104141,  1.40824239, -1.02927402,\n",
       "        0.43614147, -1.68331431, -0.18527667,  0.83437284, -0.67776796,\n",
       "        0.52516118,  0.91530124,  0.92100861, -0.87242406,  0.01241736,\n",
       "       -0.63215149, -0.91569594, -0.19178026, -0.27403778,  0.15483569,\n",
       "       -1.29268508, -1.48315324,  1.51882805,  0.91600065,  1.04115273,\n",
       "        0.57293692,  0.11671339, -0.74282968,  1.02152953, -0.97313424,\n",
       "       -0.69422819, -2.88393758, -0.34724282, -0.32770277, -0.31008446,\n",
       "       -2.06240491,  0.89283679, -1.10282868,  0.01189821, -1.44149568,\n",
       "       -0.59145564, -0.3854264 ,  0.20729091,  0.00542133,  1.15447106,\n",
       "       -1.43199155,  0.78044723, -0.68511716,  0.85299771, -1.61523274,\n",
       "        0.97595693,  0.51624195, -0.37335099, -1.27081515, -1.0321499 ,\n",
       "       -0.99731028, -0.85646209, -0.33996124, -0.00550493, -0.30440227,\n",
       "        0.86538929, -0.64707114, -1.27347534, -0.67086446, -0.44881093,\n",
       "        2.04317857, -0.45893744, -0.24786306, -1.33111148,  0.37012649,\n",
       "        2.20011182, -0.60738043, -1.98560265,  0.16274192,  1.70401112,\n",
       "       -0.13965249,  0.05365479,  0.34387945,  0.6466209 ,  1.76265587,\n",
       "        1.53852189,  0.80079245, -0.79106773,  2.2408473 ,  0.68639053,\n",
       "        0.88702032,  0.34864221, -2.83274815, -0.99786965, -1.11131874,\n",
       "        0.22653665,  0.14453828, -1.12807646,  2.73387989,  0.66551923,\n",
       "       -0.77552105, -1.24660408,  0.17520703,  0.40830438,  0.16404198,\n",
       "       -1.02756303, -0.09714543, -1.57845074, -0.63752747,  1.05367051,\n",
       "        0.60548366,  1.03690316, -0.70618405, -2.1167637 ,  0.98912976,\n",
       "        1.74060411, -0.36499934, -0.41270549, -1.7401915 ,  1.09921724,\n",
       "        1.45532839,  0.53413975,  0.11242317,  0.08704196,  0.34219354,\n",
       "       -0.23508621, -0.98963218, -0.11152983,  2.31779458, -0.05672017,\n",
       "       -1.18026675,  0.39809277, -1.36840994,  0.17183569, -0.15493595,\n",
       "        0.21464537,  1.12363796,  0.45188309,  0.6579471 ,  0.17675365,\n",
       "        0.56330542, -1.28635537, -1.1967441 , -0.50744226, -2.05710702,\n",
       "        0.44026105,  0.44744155,  0.98788986,  0.86064772,  1.51854152,\n",
       "       -1.57983867, -1.02060649,  0.37626515,  0.71448569, -0.18664445,\n",
       "       -0.15536839, -1.27778314,  0.80445741,  2.13750666,  0.17592752,\n",
       "       -1.98149076,  0.20188949, -1.05395862, -0.12909263,  0.51837378,\n",
       "        1.63294644,  0.09757401, -2.12862945, -2.12655469,  1.23608068,\n",
       "       -0.86857068,  1.5614233 , -0.33584714,  0.37692209,  1.72239804,\n",
       "        0.44240384,  0.84675674,  2.20099341, -0.88417052,  0.70205416,\n",
       "       -1.17238303,  0.47576366, -0.08679817, -0.30821028,  0.02695086,\n",
       "       -0.58199019, -0.66320909,  0.14443143, -0.19159035, -0.18826419,\n",
       "        0.57889405, -0.95343599, -1.35907224, -0.04466951,  0.72531693,\n",
       "        1.31110444,  0.37620076,  1.3531264 ,  0.78984043, -0.68762959,\n",
       "       -0.64210755,  1.24859384, -0.481854  ,  0.88556488,  0.79753399,\n",
       "        0.31301977,  0.61251785, -0.20764243,  0.15049877, -1.74416427,\n",
       "        0.05174462, -0.97633718,  0.6573566 ,  1.44045881,  0.98664144,\n",
       "       -0.9377451 , -1.85069082, -1.13823701,  0.99454937,  1.37154979,\n",
       "        1.93317188, -0.26540195, -0.8830695 , -1.02691568, -0.06715135,\n",
       "        0.40893693, -1.05819845, -0.46090771,  0.65408727,  0.74026014,\n",
       "       -0.49111088, -0.24046585,  0.3219339 , -0.0447841 , -1.03676494,\n",
       "       -0.90527516,  1.00905947, -1.59612538, -0.11217003, -0.46595424,\n",
       "        1.12264632, -0.98477744,  3.14251128, -1.31319528,  1.23949284,\n",
       "        0.07906687,  0.51517612,  0.23163745,  1.92109154, -0.3339158 ,\n",
       "        0.84024959, -0.32633925,  0.88772001,  0.91204213, -2.00636096,\n",
       "       -0.82231385, -0.27262865,  0.04831571,  0.65355272, -0.42603632,\n",
       "        2.31741247, -0.28259495, -0.18065971, -0.30463254, -0.12676065,\n",
       "       -1.06603193, -0.32658432, -0.82202972, -0.47505562,  1.70921085,\n",
       "        0.53677581,  1.48447411, -0.59032392, -0.33875842,  0.19779003,\n",
       "       -0.7393499 ,  0.56845783, -0.99403424,  1.79634293,  0.53939268,\n",
       "       -0.72481713,  2.7362689 ,  2.23058941, -0.78936639, -0.05138576,\n",
       "        0.03499331,  0.52705276, -1.74045916, -1.30242645, -0.68901697,\n",
       "        1.09729573,  0.43522624,  1.34926541,  0.34014756,  0.43051994,\n",
       "       -0.79929409,  0.14864227,  0.41740557,  1.71363571, -0.65457205,\n",
       "       -0.19264965, -0.53236577, -0.46595838,  1.12428508, -1.1210692 ,\n",
       "       -0.54085192, -1.39591783,  0.21704335, -0.13811385,  0.63466898,\n",
       "        0.32734913,  0.53665293, -1.96353995, -0.40402376,  0.375616  ,\n",
       "        0.16219161, -0.03639462, -0.29662316,  1.05192883, -1.91992881,\n",
       "        1.9290971 , -1.53555173, -1.38362193,  1.84803056,  0.76318353,\n",
       "       -0.37561095, -0.24911264, -0.90292043,  0.81502806,  1.52377608,\n",
       "        0.44294858,  1.47641089,  1.5573205 , -0.70724238, -0.81560278,\n",
       "       -0.04203656, -0.96318323, -0.38773368,  0.27651804,  0.42026768,\n",
       "        1.18236869,  0.93214074,  0.81294749, -0.42158185,  0.18357129,\n",
       "       -0.27395708,  0.87105783,  1.20951044, -0.60225618, -0.18621286,\n",
       "       -0.16650221,  0.07403613, -1.38517399, -2.31202784, -1.57241181,\n",
       "       -0.21099822, -2.31446178,  1.64698248, -0.46654969, -0.9015564 ,\n",
       "       -0.3397874 , -0.66107832,  0.35416155, -0.16626899, -0.1684055 ])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy.stats import norm\n",
    "# Create a NumPy array with 1000 samples from a normal distribution\n",
    "data = np.random.normal(loc=0, scale=1, size=1000)\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "de6c97a3-12d2-44d9-a066-466a8b58a7e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0.00465906, 0.00465906, 0.01863622, 0.00931811, 0.02329528,\n",
       "        0.06522677, 0.07454488, 0.0931811 , 0.16772598, 0.13977165,\n",
       "        0.29352047, 0.33079291, 0.28886141, 0.34942913, 0.40533779,\n",
       "        0.3634063 , 0.34011102, 0.39136063, 0.28886141, 0.28886141,\n",
       "        0.19102126, 0.13045354, 0.13045354, 0.11181732, 0.05590866,\n",
       "        0.03261339, 0.02329528, 0.00931811, 0.02795433, 0.00465906]),\n",
       " array([-3.29656264, -3.08192684, -2.86729104, -2.65265525, -2.43801945,\n",
       "        -2.22338365, -2.00874786, -1.79411206, -1.57947626, -1.36484046,\n",
       "        -1.15020467, -0.93556887, -0.72093307, -0.50629727, -0.29166148,\n",
       "        -0.07702568,  0.13761012,  0.35224592,  0.56688171,  0.78151751,\n",
       "         0.99615331,  1.2107891 ,  1.4254249 ,  1.6400607 ,  1.8546965 ,\n",
       "         2.06933229,  2.28396809,  2.49860389,  2.71323969,  2.92787548,\n",
       "         3.14251128]),\n",
       " <BarContainer object of 30 artists>)"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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igodO3ZMMTExysrK0quvvqqnnnrKO+fs2bNauHCh2tvbFR8fr0mTJmnPnj269957Q3CKAAAAiCQBbZIqLS1VaWnpgM/V1dX5PF6yZInPaulAVq9e3e/uUgAAALgxBXSrUwAAAGCwEFABAABglIA+4gcARB63u0ctLS1B1eBOWQCuBwIqANwAus6e0bEjR1X58itB3eSEO2UBuB4IqABwA+j+8ryGDR+u+22LdMvYrIDrcKcsANcDARUAbiAJKaODulsWd8oCcD2wSQoAAABGIaACAADAKARUAAAAGIWACgAAAKMQUAEAAGAUAioAAACMwmWmAFx3TqdTLpcr6DpWq1VJSUkh6AgAYBICKoDryul06smFJeq60B10rZEj4rShdj0hFQCGGAIqgOvK5XKp60K3HrAtUkJqWsB1Tjs+1663a+RyuQioADDEEFABhEVCalpQdzQCAAxdbJICAACAUQioAAAAMAoBFQAAAEYhoAIAAMAoBFQAAAAYhYAKAAAAoxBQAQAAYBQCKgAAAIxCQAUAAIBRCKgAAAAwCgEVAAAARiGgAgAAwCgEVAAAABiFgAoAAACjEFABAABgFAIqAAAAjEJABQAAgFEIqAAAADAKARUAAABGIaACAADAKARUAAAAGIWACgAAAKMQUAEAAGAUAioAAACMQkAFAACAUQioAAAAMAoBFQAAAEYJKKBWV1crMzNTcXFxysnJ0d69e684d9++fZo6daoSEhI0YsQIZWdna/Xq1f3mbdmyRRMmTJDFYtGECRO0devWQFoDAABAhPM7oNbX16usrEyVlZVqampSQUGBZs+erdbW1gHn33TTTXr66ae1Z88effrpp1q2bJmWLVum2tpa75wDBw6oqKhINptNhw4dks1m07x58/TRRx8FfmYAAACISH4H1FWrVqm4uFgLFizQ+PHjZbfblZ6erpqamgHnT5o0SY888oi+853vaOzYsXrsscc0a9Ysn1VXu92umTNnqqKiQtnZ2aqoqNCMGTNkt9sDPjEAAABEJr8CqtvtVmNjowoLC33GCwsLtX///muq0dTUpP379+v+++/3jh04cKBfzVmzZl21Zk9Pj1wul88BAACAyOdXQO3o6FBfX5+Sk5N9xpOTk9Xe3n7V16alpclisSg3N1eLFy/WggULvM+1t7f7XbOqqkrx8fHeIz093Z9TAQAAgKEC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\n",
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot a histogram of the data with 30 bins\n",
    "plt.figure(figsize=(8, 6))\n",
    "plt.hist(data, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5c44796f-c15c-4221-9633-52ab679385da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7ff7c66c15a0>]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiwAAAGdCAYAAAAxCSikAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8o6BhiAAAACXBIWXMAAA9hAAAPYQGoP6dpAABO6klEQVR4nO3deVhUdcM+8HsYYEAMcsUFJCRNFDXBBFREHxXFFVe0xD1FsXDLVwPLzMRU1BZBQdFEWdxXEMY0RDFNwrRHUnPDBXIH3FiG8/uDn+d9R0QZAs7McH+u61xd5ztnTvc5j09ze+bM98gEQRBAREREpMUMpA5ARERE9CYsLERERKT1WFiIiIhI67GwEBERkdZjYSEiIiKtx8JCREREWo+FhYiIiLQeCwsRERFpPUOpA1SUoqIi3L59G2+99RZkMpnUcYiIiKgMBEFAbm4uGjVqBAOD0q+j6E1huX37NqytraWOQUREROVw48YNWFlZlfq63hSWt956C0DxAZubm0uchoiIiMoiJycH1tbW4ud4afSmsLz4Gsjc3JyFhYiISMe86XYO3nRLREREWo+FhYiIiLQeCwsRERFpPRYWIiIi0nosLERERKT1WFiIiIhI67GwEBERkdYrV2EJCQmBra0tTExM4OTkhOTk5DK97/jx4zA0NMT7779f4rUdO3agZcuWUCgUaNmyJXbt2lWeaERERKSHNC4ssbGxmD59OgICApCWlgY3Nzd4enoiIyPjte/Lzs7G6NGj0b179xKvnThxAt7e3vDx8cEff/wBHx8fDB8+HCdPntQ0HhEREekhmSAIgiZvcHZ2hqOjI0JDQ8Uxe3t7eHl5ISgoqNT3jRgxAs2aNYNcLsfu3btx5swZ8TVvb2/k5OQgPj5eHOvduzdq1aqF6OjoMuXKycmBhYUFsrOzOdMtERGRjijr57dGV1jy8/ORmpoKDw8PtXEPDw+kpKSU+r4NGzbg8uXL+PLLL1/5+okTJ0rss1evXq/dZ15eHnJyctQWIiIi0k8aFZZ79+5BpVLB0tJSbdzS0hJZWVmvfM+lS5cwd+5cbNmyBYaGr350UVZWlkb7BICgoCBYWFiIC5/UTEREpL/K9fDDlx9QJAjCKx9apFKp8OGHH+Krr75C8+bNK2SfL8ybNw8zZ84U11887bEi3bp1C23btoWBgQHkcrnaP42NjaFQKGBiYiL+s2bNmnjrrbdQs2ZN1KxZE+bm5qhVq5a41K5dG/Xq1YOlpSXMzMze+KAnIiIiKqZRYalbty7kcnmJKx937twpcYUEAHJzc3H69GmkpaVh2rRpAICioiIIggBDQ0MkJibiP//5Dxo0aFDmfb6gUCigUCg0ia+xgoIC3L9/v1L2bWpqivr168PS0hKNGzdG48aN0ahRIzRu3Bg2NjZ455130Lhx41KvShEREVUnGn0aGhsbw8nJCUqlEoMGDRLHlUolBg4cWGJ7c3NznDt3Tm0sJCQEhw8fxvbt22FrawsAcHV1hVKpxIwZM8TtEhMT0bFjR40OpqLJ5XK8++67UKlUKCoqUvtnfn4+8vLy8Pz5cxQVFWm872fPnuH69eu4fv36a//91tbWsLW1xbvvvot3330XzZo1E/9pYmLybw6PiIhIZ2j81/eZM2fCx8cH7du3h6urK8LCwpCRkQFfX18AxV/V3Lp1C5s2bYKBgQEcHBzU3l+/fn2YmJiojfv7+6NLly749ttvMXDgQOzZsweHDh3CsWPH/uXh/TvW1ta4dOnSG7crLCzEs2fP8OTJE+Tm5uLx48fIzc1FdnY2Hj58KC4PHjzA3bt3cefOHdy5cwf//PMP7t27h9J+qKVSqXDt2jVcu3YNR44cUXvNwMAAtra2aNmyJezt7dGyZUu0adMG9vb2LDJERKR3NC4s3t7euH//PhYuXIjMzEw4ODggLi4ONjY2AIDMzMw3zsnyso4dOyImJgaBgYGYP38+7OzsEBsbC2dnZ03jScLQ0BBvvfUW3nrrLTRo0ECj9xYUFCAzMxO3bt3CrVu3cPPmTWRkZIhF5erVq3j06FGJ9xUVFeHy5cu4fPky9u3bJ47L5XK0aNECbdq0wfvvvw8nJyc4OjqiVq1a//YwiYiIJKPxPCzaSp/nYXn48CH+/vtvcbl48SL++usvpKen48mTJ2Xah52dHdq3bw9nZ2e4uLigXbt2vBJDRESSK+vnNwuLDisqKsKNGzeQnp6OP//8E2fPnsUff/yB9PR0FBQUvPa9RkZGaNeuHVxdXdG5c2e4ubm99iZnIiKiysDCUo3l5+fjr7/+wu+//47Tp08jNTUVZ86cwfPnz1/7vmbNmqFz587o1q0bunXrBisrqypKTERE1RULC6kpLCzEn3/+iZMnT+LXX3/FyZMnkZ6e/tr3NGvWDN26dUP37t3RvXt31KlTp4rSEhFRdcHCQm/08OFDpKSk4NixY0hOTsZvv/2G/Pz8V24rk8nQvn17eHh4wMPDA66urjAyMqrixEREpG9YWEhjz58/x6+//oojR47gyJEj+PXXX0u9F8bc3BweHh7o27cvPD09ef8LERGVCwsL/WtPnjzB8ePHcejQISQkJODs2bOlbtuhQwcMHDgQXl5esLe352MHiIioTFhYqMJlZmbi0KFDOHjwIA4ePIgHDx68crt3330XXl5eGDRoEFxcXGBgoNEzNomIqBphYaFKVVhYiJMnT+LAgQM4cOBAqVdfGjdujCFDhmDYsGHo2LEjywsREalhYaEqde3aNezZswe7d+9GcnIyVCpViW0aNmyI4cOHY+TIkejQoQO/NiIiIhYWks79+/exb98+7NixA4mJia/85VHTpk0xYsQIfPTRR2jZsqUEKYmISBuwsJBWyM7Oxt69e7Ft2zYkJCS8srw4Ojpi9OjRGDlyJOrXry9BSiIikgoLC2mdR48eYefOnYiOjsbhw4dRVFSk9rpcLkfv3r0xbtw49O/fH8bGxhIlJSKiqsLCQlrtn3/+wdatWxEZGYnffvutxOt169bFqFGjMGHCBDg4OEiQkIiIqgILC+mM9PR0REZGIjIyEjdv3izxeocOHTBp0iSMGDECZmZmEiQkIqLKwsJCOqeoqAg///wzIiIisGvXLuTl5am9bm5ujlGjRmHSpElo27atRCmJiKgisbCQTnvw4AGioqKwbt06/PHHHyVed3V1xbRp0zB06FDe60JEpMNYWEgvCIKA3377DWFhYYiOjsbTp0/VXq9fvz4+/vhj+Pr6wsrKSqKURERUXiwspHeys7OxZcsWhIaG4s8//1R7TS6XY+jQoZg+fTpcXFwkSkhERJoq6+c350knnWFhYYGpU6fi7NmzSEpKwrBhwyCXywEAKpUKsbGxcHV1hbOzM6Kjo0t90jQREekeXmEhnXb79m2sXbsWoaGhuHv3rtprVlZWmD59Oj7++GP+mSAi0lL8SoiqlefPnyMmJgarVq0qcZOuubk5Jk+ejE8//ZT3uRARaRl+JUTViomJCcaOHYu0tDQcOXIE/fv3F1/LycnBsmXLYGtri3HjxuGvv/6SMCkREZUHCwvpFZlMhq5du2Lv3r1IT0/Hxx9/DIVCAQAoLCzExo0b0bJlSwwZMgSnT5+WOC0REZUVCwvprRYtWiAsLAzXr19HQEAA3n77bQDFP5XeuXMnPvjgA3h4eCA5OVnaoERE9EYsLKT3LC0tsWjRIly/fh1Lly5FgwYNxNeUSiW6dOmCrl274vDhw9CTW7qIiPQOCwtVG+bm5vjss89w9epVrF27Fk2bNhVfS0pKQvfu3dG5c2colUoWFyIiLcPCQtWOiYkJJk2ahAsXLuCnn35C8+bNxddSUlLg4eEBNzc3XnEhItIiLCxUbRkaGmL06NE4f/48oqOj0apVK/G148ePo3v37ujatSuOHj0qYUoiIgJYWIggl8sxYsQInD17FrGxsbC3txdfO3r0KNzd3dGrVy/+qoiISEIsLET/n4GBAYYPH45z585hy5Ytal8VJSYm4oMPPsCQIUNw/vx5CVMSEVVPLCxEL5HL5fjwww/x3//+Fxs3bsQ777wjvrZz5060bt0a48aNQ0ZGhnQhiYiqGRYWolIYGhpizJgxuHDhAlavXi3+HLqoqAgbN25E8+bNMWfOHDx48EDipERE+q9chSUkJAS2trYwMTGBk5PTayfeOnbsGDp16oQ6derA1NQULVq0wMqVK0tst2rVKrz33nswNTWFtbU1ZsyYgefPn5cnHlGFMjY2xtSpU3H58mUsWbJEnIAuLy8Py5Ytg52dHZYuXco/r0RElUnQUExMjGBkZCSEh4cL58+fF/z9/QUzMzPh+vXrr9z+999/F6KiooQ///xTuHr1qhAZGSnUqFFDWLt2rbjN5s2bBYVCIWzZskW4evWqkJCQIDRs2FCYPn16mXNlZ2cLAITs7GxND4lIIw8ePBDmzJkjKBQKAYC42NjYCFFRUYJKpZI6IhGRzijr57fGT2t2dnaGo6MjQkNDxTF7e3t4eXkhKCioTPsYPHgwzMzMEBkZCQCYNm0a0tPT8fPPP4vbzJo1C6dOnSrztOl8WjNVtRs3buDLL7/ETz/9hKKiInH8gw8+QHBwMNzc3CRMR0SkGyrlac35+flITU2Fh4eH2riHhwdSUlLKtI+0tDSkpKTA3d1dHOvcuTNSU1Nx6tQpAMCVK1cQFxeHvn37lrqfvLw85OTkqC1EVcna2hoRERE4c+YMevXqJY7/9ttv6NKlC4YMGYIrV65ImJCISH9oVFju3bsHlUoFS0tLtXFLS0tkZWW99r1WVlZQKBRo3749/Pz8MHHiRPG1ESNG4Ouvv0bnzp1hZGQEOzs7dOvWDXPnzi11f0FBQbCwsBAXa2trTQ6FqMK0bt0aBw8exMGDB9G6dWtxfOfOnbC3t8e8efOQm5srYUIiIt1XrptuZTKZ2rogCCXGXpacnIzTp09jzZo1WLVqFaKjo8XXfvnlF3zzzTcICQnB77//jp07d2L//v34+uuvS93fvHnzkJ2dLS43btwoz6EQVZhevXohLS0N4eHhYqnPz8/HkiVL0KxZM0RERKh9dURERGWn0T0s+fn5qFGjBrZt24ZBgwaJ4/7+/jhz5gySkpLKtJ9FixYhMjISFy5cAAC4ubnBxcUFy5YtE7fZvHkzJk2ahMePH8PA4M29ivewkDbJycnB4sWLsXLlSuTn54vjH3zwAX744Qc4OztLmI6ISHtUyj0sxsbGcHJyglKpVBtXKpXo2LFjmfcjCALy8vLE9adPn5YoJXK5HIIg8OFzpJPMzc2xZMkSpKenY/DgweL4b7/9BhcXF4wfPx7//POPhAmJiHSLxl8JzZw5E+vWrUNERATS09MxY8YMZGRkwNfXF0DxVzWjR48Wt1+9ejX27duHS5cu4dKlS9iwYQOWL1+OUaNGidv0798foaGhiImJwdWrV6FUKjF//nwMGDAAcrm8Ag6TSBpNmzbFjh07cPjwYTg4OIjjGzZsQPPmzbFq1SoUFhZKmJCISEeU5zfTq1evFmxsbARjY2PB0dFRSEpKEl8bM2aM4O7uLq5///33QqtWrYQaNWoI5ubmQrt27YSQkBC1uSoKCgqEBQsWCHZ2doKJiYlgbW0tTJ06VXj48GGZM3EeFtJ2BQUFwnfffSdYWFiozd/Spk0b4dixY1LHIyKSRKXNw6KteA8L6Yq7d+/i888/x/r169W+8hw7diy+/fZb1K9fX8J0RERVq1LuYSGif69evXoIDw/HiRMn4OjoKI5v3LgR7733HtauXctfExERvYSFhUgizs7OOHXqFH788UdYWFgAAB49egRfX1907twZ586dkzghEZH2YGEhkpBcLoefnx8uXLgAHx8fcfzEiRNo164d5syZgydPnkiYkIhIO7CwEGkBS0tLbNq0CYcPH0bz5s0BACqVCsuWLYODgwMSEhIkTkhEJC0WFiIt0q1bN5w9exZfffUVFAoFAODatWvo3bs3Ro0ahbt370qckIhIGiwsRFpGoVDgiy++wNmzZ9GtWzdxfMuWLbC3t8emTZs4oSIRVTssLERaqnnz5vj5558RERGBWrVqAQDu37+PMWPGwNPTE9evX5c4IRFR1WFhIdJiMpkM48aNQ3p6OkaMGCGOJyQkoFWrVli9ejV/Ak1E1QILC5EOsLS0RHR0NPbv3w8rKysAwJMnTzBt2jS4u7uLDxIlItJXLCxEOqRv3774888/MWnSJHHs2LFjeP/99xEcHAyVSiVhOiKiysPCQqRjLCwssHbtWhw+fBhNmzYFADx//hyzZ89Gly5dcPHiRYkTEhFVPBYWIh314ifQ/v7+kMlkAICUlBS0bdsWK1as4NUWItIrLCxEOszMzAyrVq1CUlIS7OzsABRfbZk1axa6du2Ky5cvS5yQiKhisLAQ6QE3N7cSV1uOHTuGtm3bYs2aNZy3hYh0HgsLkZ6oUaOGeLXF1tYWQPEviaZMmQJPT0/cunVL4oREROXHwkKkZ15cbZk8ebI4lpCQAAcHB8TExEiYjIio/FhYiPRQzZo1sWbNGsTHx6NRo0YAgEePHmHkyJH46KOP8PDhQ4kTEhFphoWFSI/17t0bf/75J0aOHCmORUVFoU2bNjh8+LCEyYiINMPCQqTnatWqhaioKERFRcHCwgIAcPPmTXTv3h2zZs1CXl6exAmJiN6MhYWomhg5ciTOnTuH//znP+LYihUr4OLigvT0dAmTERG9GQsLUTVibW0NpVKJFStWwNjYGABw5swZODo6IjQ0lD9/JiKtxcJCVM0YGBhgxowZOHXqFFq2bAmgeLK5qVOnYuDAgbh7967ECYmISmJhIaqm2rZti9OnT2PatGni2L59+9C2bVvekEtEWoeFhagaMzU1xQ8//ID9+/ejXr16AIDMzEz06NEDn3/+OQoKCiROSERUjIWFiNC3b1/88ccf6NGjBwBAEAQEBQXBzc0NV69elTgdERELCxH9fw0bNkRCQgK+/fZbGBoaAgBOnjyJdu3aYfv27RKnI6LqjoWFiEQGBgaYM2cOjh8/jqZNmwIAsrOzMWzYMPj5+eH58+cSJySi6oqFhYhK6NChA9LS0jBixAhxLCQkBC4uLrh48aKEyYioumJhIaJXMjc3R1RUFMLDw2FiYgIA+OOPP+Do6IioqCiJ0xFRdcPCQkSlkslkmDhxIk6dOgV7e3sAwJMnT/DRRx9h8uTJ/IqIiKoMCwsRvVHr1q3x22+/YezYseJYWFgYXF1d8ffff0sXjIiqDRYWIioTMzMzbNiwARERETA1NQXwv9P6b9u2TeJ0RKTvylVYQkJCYGtrCxMTEzg5OSE5ObnUbY8dO4ZOnTqhTp06MDU1RYsWLbBy5coS2z169Ah+fn5o2LAhTExMYG9vj7i4uPLEI6JKNG7cOJw6dQrvvfceACA3NxfDhw/HjBkzONEcEVUajQtLbGwspk+fjoCAAKSlpcHNzQ2enp7IyMh45fZmZmaYNm0ajh49ivT0dAQGBiIwMBBhYWHiNvn5+ejZsyeuXbuG7du348KFCwgPD0fjxo3Lf2REVGkcHBxw+vRpfPjhh+LYqlWr0LVrV9y8eVPCZESkr2SCho9ndXZ2Fp/s+oK9vT28vLwQFBRUpn0MHjwYZmZmiIyMBACsWbMGy5Ytw19//QUjIyNN4ohycnJgYWGB7OxsmJubl2sfRKQZQRCwdu1a+Pv7Iz8/HwBQr149REVFibPmEhG9Tlk/vzW6wpKfn4/U1FR4eHiojXt4eCAlJaVM+0hLS0NKSgrc3d3Fsb1798LV1RV+fn6wtLSEg4MDFi9eDJVKVep+8vLykJOTo7YQUdWSyWTw9fXFsWPHYGNjAwC4e/cuPDw8sHjxYhQVFUmckIj0hUaF5d69e1CpVLC0tFQbt7S0RFZW1mvfa2VlBYVCgfbt28PPzw8TJ04UX7ty5Qq2b98OlUqFuLg4BAYGIjg4GN98802p+wsKCoKFhYW4WFtba3IoRFSBPvjgA6SmpsLT0xNA8ZWXgIAADB48GNnZ2RKnIyJ9UK6bbmUymdq6IAglxl6WnJyM06dPY82aNVi1ahWio6PF14qKilC/fn2EhYXByckJI0aMQEBAgNrXTi+bN28esrOzxeXGjRvlORQiqiB16tTB/v37sXDhQvG/B3v27MEHH3yAP//8U+J0RKTrDDXZuG7dupDL5SWupty5c6fEVZeX2draAiiez+Gff/7BggULMHLkSADFD10zMjKCXC4Xt7e3t0dWVhby8/NhbGxcYn8KhQIKhUKT+ERUyQwMDDB//nx88MEH+PDDD/Hw4UNcunQJzs7OWL9+vdpU/0REmtDoCouxsTGcnJygVCrVxpVKJTp27Fjm/QiCgLy8PHG9U6dO+Pvvv9W+77548SIaNmz4yrJCRNqtd+/eSE1NRbt27QAAT58+xciRIzF79mwUFhZKnI6IdJHGXwnNnDkT69atQ0REBNLT0zFjxgxkZGTA19cXQPFXNaNHjxa3X716Nfbt24dLly7h0qVL2LBhA5YvX45Ro0aJ20yZMgX379+Hv78/Ll68iAMHDmDx4sXw8/OrgEMkIinY2tri+PHjarPjBgcHo1evXrh37550wYhIJ2n0lRAAeHt74/79+1i4cCEyMzPh4OCAuLg48RcCmZmZanOyFBUVYd68ebh69SoMDQ1hZ2eHJUuWYPLkyeI21tbWSExMxIwZM9CmTRs0btwY/v7++J//+Z8KOEQikoqpqSkiIiLQoUMHfPrppygsLMThw4fh5OSEXbt2wdHRUeqIRKQjNJ6HRVtxHhYi7Xbs2DEMHToU//zzDwDAxMQEYWFh8PHxkTgZEUmpUuZhISIqr86dOyM1NRUuLi4AgOfPn2P06NGYNWsW72shojdiYSGiKtO4cWP88ssv+Pjjj8WxFStWoE+fPnjw4IGEyYhI27GwEFGVUigUWLt2LUJCQmBoWHwbnVKp5HwtRPRaLCxEVOVkMhmmTJmCn3/+GfXq1QNQPOO1i4sL9uzZI3E6ItJGLCxEJJkuXbrg9OnT4q+Fnjx5Ai8vL3zzzTfQk98DEFEFYWEhIkk1adIEycnJarPgBgYG4sMPP8TTp08lTEZE2oSFhYgkV6NGDURFRak98DQmJgZdunTBzZs3JUxGRNqChYWItIJMJsPnn3+O3bt3o2bNmgCA1NRUdOjQAb/99pvE6YhIaiwsRKRVBg4ciJSUFPGBqZmZmejSpQtiY2MlTkZEUmJhISKt07p1a5w6dQpubm4AiieZGzFiBBYsWMCbcYmqKRYWItJKdevWhVKpxLhx48Sxr776CiNGjMCzZ88kTEZEUmBhISKtpVAosH79eixbtgwymQwAsHXrVnTt2hVZWVkSpyOiqsTCQkRaTSaTYfbs2di7d694M+6pU6fg7OyMs2fPSpyOiKoKCwsR6YR+/frh+PHjsLa2BgBkZGSgU6dOiIuLkzgZEVUFFhYi0hlt2rTByZMn8cEHHwAAHj9+jP79++P777+XOBkRVTYWFiLSKQ0bNsQvv/yCoUOHAgCKiorg7++PTz/9FCqVSuJ0RFRZWFiISOfUqFEDsbGxmDdvnjj2ww8/YNCgQXj8+LGEyYiosrCwEJFOMjAwwOLFi7F+/XoYGhoCAPbt24cuXbrg9u3bEqcjoorGwkJEOm38+PE4ePAgLCwsAABpaWn8BRGRHmJhISKd1717d6SkpMDGxgYAcPPmTXTu3BlKpVLiZERUUVhYiEgvtGzZUu0XRLm5uejTpw82bNggcTIiqggsLESkNywtLXHkyBEMHDgQAFBYWIjx48fjyy+/5DOIiHQcCwsR6RUzMzPs2LEDn3zyiTi2cOFCjB07Fvn5+RImI6J/g4WFiPSOXC7Hd999hxUrVojPINq0aRP69euHnJwcidMRUXmwsBCRXpLJZJgxYwa2bdsGhUIBAFAqlXB3d+fPnol0EAsLEem1IUOG4Oeff0bt2rUBAGfOnIGrqyvS09MlTkZEmmBhISK916lTJxw/fhzvvPMOgOIHJ3bs2BHJycnSBiOiMmNhIaJqoUWLFjhx4gTatWsHAHj06BF69uyJnTt3SpyMiMqChYWIqo0GDRogKSkJvXr1AgDk5eVh6NChCAkJkTgZEb0JCwsRVStvvfUW9u3bh9GjRwMABEGAn58fAgICOFcLkRZjYSGiasfIyAgbN27E3LlzxbHFixdjwoQJKCwslDAZEZWmXIUlJCQEtra2MDExgZOT02tvXDt27Bg6deqEOnXqwNTUFC1atMDKlStL3T4mJgYymQxeXl7liUZEVCYymQxBQUH44YcfxLlaNmzYgEGDBuHp06cSpyOil2lcWGJjYzF9+nQEBAQgLS0Nbm5u8PT0REZGxiu3NzMzw7Rp03D06FGkp6cjMDAQgYGBCAsLK7Ht9evXMXv2bLi5uWl+JERE5TBt2jRs3boVxsbGAID9+/ejR48eePDggcTJiOj/kgkafmnr7OwMR0dHhIaGimP29vbw8vJCUFBQmfYxePBgmJmZITIyUhxTqVRwd3fHuHHjkJycjEePHmH37t1lzpWTkwMLCwtkZ2fD3Ny8zO8jIgIgPoMoNzcXQPF/1xISEmBtbS1xMiL9VtbPb42usOTn5yM1NRUeHh5q4x4eHkhJSSnTPtLS0pCSkgJ3d3e18YULF6JevXqYMGGCJpGIiCpEt27dkJSUBEtLSwBAeno6OnbsiPPnz0ucjIgADQvLvXv3oFKpxP9Dv2BpaYmsrKzXvtfKygoKhQLt27eHn58fJk6cKL52/PhxrF+/HuHh4WXOkpeXh5ycHLWFiOjfaNeuHY4fPw47OzsAwM2bN+Hm5oaTJ09KnIyIynXT7Ysb1F4QBKHE2MuSk5Nx+vRprFmzBqtWrUJ0dDQAIDc3F6NGjUJ4eDjq1q1b5gxBQUGwsLAQF162JaKKYGdnh+PHj4sTzD148ADdu3dHYmKixMmIqjeN7mHJz89HjRo1sG3bNgwaNEgc9/f3x5kzZ5CUlFSm/SxatAiRkZG4cOECzpw5g3bt2kEul4uvFxUVAQAMDAxw4cIF8W87/1deXh7y8vLE9ZycHFhbW/MeFiKqEDk5ORg4cCB++eUXAMU/hd68eTOGDx8ubTAiPVMp97AYGxvDyckJSqVSbVypVKJjx45l3o8gCGLZaNGiBc6dO4czZ86Iy4ABA9CtWzecOXOm1CsnCoUC5ubmagsRUUUxNzdHfHy8+JezgoICjBgxQu0HB0RUdQw1fcPMmTPh4+OD9u3bw9XVFWFhYcjIyICvry8AYN68ebh16xY2bdoEAFi9ejWaNGmCFi1aACiel2X58uX45JNPAAAmJiZwcHBQ+3e8/fbbAFBinIioKpmYmGDr1q3w9fXF+vXrIQgCpk6divv37yMgIOCNX4UTUcXRuLB4e3vj/v37WLhwITIzM+Hg4IC4uDjY2NgAADIzM9XmZCkqKsK8efNw9epVGBoaws7ODkuWLMHkyZMr7iiIiCqJoaEhwsPDUa9ePSxZsgQAMH/+fDx48ADLly+HgQEnDCeqChrPw6KtOA8LEVW25cuX47PPPhPXx44di/DwcBgaavx3PyL6/yrlHhYioups9uzZWLdunXhVZePGjRg2bBieP38ucTIi/cfCQkSkgQkTJqhN5b9792706dNHnCGXiCoHCwsRkYaGDBmC/fv3w8zMDEDxtP49e/bk84eIKhELCxFROfTs2ROHDh0Sf9V48uRJdO3a9Y2zfhNR+bCwEBGVk4uLi9rzh86dOwc3Nzdcv35d4mRE+oeFhYjoX2jTpg2Sk5PRpEkTAMDff/+Nzp0748KFCxInI9IvLCxERP9Ss2bNcOzYMbz33nsAih+a2KVLF5w9e1biZET6g4WFiKgCWFtb4+jRo3j//fcBAHfu3EHXrl1x6tQpaYMR6QkWFiKiClK/fn0cOXIELi4uAICHDx+ie/fuZX4wLBGVjoWFiKgCvf3221AqlejWrRsA4PHjx+jduzfi4+MlTkak21hYiIgqWM2aNXHgwAH07dsXAPD8+XMMHDgQu3btkjgZke5iYSEiqgSmpqbYuXMnhg0bBgAoKCjAsGHDEBUVJXEyIt3EwkJEVEmMjY0RFRWF0aNHAwBUKhVGjRqFiIgIiZMR6R4WFiKiSmRoaIgNGzbA19cXACAIAiZMmIAff/xR4mREuoWFhYiokhkYGCAkJAQzZswQxz755BMsW7ZMwlREuoWFhYioCshkMgQHByMwMFAcmzNnDhYtWiRhKiLdwcJCRFRFZDIZvv76a3zzzTfi2Pz58xEYGAhBECRMRqT9WFiIiKrY559/juXLl4vr33zzDebMmcPSQvQaLCxERBKYNWuW2o23y5cvx6effsrSQlQKFhYiIon4+fkhLCwMMpkMAPDjjz9iypQpKCoqkjgZkfZhYSEiktDHH3+Mn376CQYGxf85Xrt2LT7++GOoVCqJkxFpFxYWIiKJ+fj4YPPmzZDL5QCAiIgIjBs3jqWF6P9gYSEi0gIjR45EdHQ0DA0NAQCRkZHw8fFBYWGhxMmItAMLCxGRlhg2bBi2bt0KIyMjAEB0dDQ+/PBDFBQUSJyMSHosLEREWmTQoEHYsWMHjI2NAQDbtm3DyJEjWVqo2mNhISLSMv3798fu3buhUCgAADt27IC3tzfy8/MlTkYkHRYWIiIt5OnpiT179oilZdeuXRg+fDhLC1VbLCxERFqqV69e2LdvH0xMTAAAe/bswZAhQ5CXlydxMqKqx8JCRKTFevbsif3798PU1BQAsH//fgwdOpSlhaodFhYiIi3XvXt3HDhwQK208EoLVTcsLEREOqBbt26Ii4sTS8uBAwdYWqhaYWEhItIRXbt2RVxcHGrUqAGApYWql3IVlpCQENja2sLExAROTk5ITk4uddtjx46hU6dOqFOnDkxNTdGiRQusXLlSbZvw8HC4ubmhVq1aqFWrFnr06IFTp06VJxoRkV5jaaHqSuPCEhsbi+nTpyMgIABpaWlwc3ODp6cnMjIyXrm9mZkZpk2bhqNHjyI9PR2BgYEIDAxEWFiYuM0vv/yCkSNH4siRIzhx4gSaNGkCDw8P3Lp1q/xHRkSkp9zd3UuUFt6IS/pOJgiCoMkbnJ2d4ejoiNDQUHHM3t4eXl5eCAoKKtM+Bg8eDDMzM0RGRr7ydZVKhVq1auHHH3/E6NGjy7TPnJwcWFhYIDs7G+bm5mV6DxGRLktKSkKfPn3w9OlTAMCAAQOwbds2cZZcIl1Q1s9vja6w5OfnIzU1FR4eHmrjHh4eSElJKdM+0tLSkJKSAnd391K3efr0KQoKClC7du1St8nLy0NOTo7aQkRUnbi7u6v9emjv3r2cXI70lkaF5d69e1CpVLC0tFQbt7S0RFZW1mvfa2VlBYVCgfbt28PPzw8TJ04sddu5c+eicePG6NGjR6nbBAUFwcLCQlysra01ORQiIr3QtWtXtXla9uzZA29vbz57iPROuW66lclkauuCIJQYe1lycjJOnz6NNWvWYNWqVYiOjn7ldkuXLkV0dDR27twpzu74KvPmzUN2dra43LhxQ/MDISLSA//5z3/UZsTdvXs3H5hIekejwlK3bl3I5fISV1Pu3LlT4qrLy2xtbdG6dWt8/PHHmDFjBhYsWFBim+XLl2Px4sVITExEmzZtXrs/hUIBc3NztYWIqLrq3r27WmnZsWMHfHx8UFhYKHEyooqhUWExNjaGk5MTlEql2rhSqUTHjh3LvB9BEErczb5s2TJ8/fXXOHjwINq3b69JLCIiAtCjRw+1BybGxsZizJgxUKlUEicj+vcMNX3DzJkz4ePjg/bt28PV1RVhYWHIyMiAr68vgOKvam7duoVNmzYBAFavXo0mTZqgRYsWAIrnZVm+fDk++eQTcZ9Lly7F/PnzERUVhXfeeUe8glOzZk3UrFnzXx8kEVF14eHhgZ07d2LQoEHIz89HVFQU5HI5NmzYALlcLnU8onLTuLB4e3vj/v37WLhwITIzM+Hg4IC4uDjY2NgAADIzM9XmZCkqKsK8efNw9epVGBoaws7ODkuWLMHkyZPFbUJCQpCfn4+hQ4eq/bu+/PLLV351REREpevTpw+2b9+OIUOGoKCgAJGRkTA0NMS6detgYMAJzkk3aTwPi7biPCxEROp2796NYcOGifexTJo0CaGhoSwtpFUqZR4WIiLSHV5eXoiJiRG/CgoLC8Onn34KPfl7KlUzLCxERHpsyJAh2Lx5s3hVZfXq1Zg5cyZLC+kcFhYiIj03YsQIbNy4UZwva9WqVZg7dy5LC+kUFhYiomrAx8cH69atE9eXLl3KHzWQTmFhISKqJsaPH4+1a9eK6wsXLsTixYslTERUdiwsRETVyKRJk/D999+L6wEBAVixYoWEiYjKhoWFiKia+eSTT7Bs2TJxfdasWVi9erWEiYjejIWFiKgamj17Nr7++mtxfdq0aWr3uBBpGxYWIqJqKjAwEAEBAeL6pEmTsHnzZgkTEZWOhYWIqBr7+uuvMWvWLADFD6YdM2YMtm/fLnEqopJYWIiIqjGZTIZly5Zh6tSpAIqf/zZy5Ejs379f4mRE6lhYiIiqOZlMhh9++AHjx48HABQWFmLIkCFQKpUSJyP6XywsREQEAwMDhIWFYeTIkQCA/Px8DBw4EEePHpU4GVExFhYiIgIAyOVy/PTTTxg0aBAA4NmzZ+jXrx9OnTolcTIiFhYiIvo/jIyMEB0dDU9PTwBAbm4uevfujbNnz0qcjKo7FhYiIlKjUCiwY8cOdO3aFQDw8OFD9OjRA3/99Ze0wahaY2EhIqISTE1NsXfvXri4uAAA7t69i+7du+PKlSsSJ6PqioWFiIhe6a233kJ8fDzef/99AMDt27fRvXt33Lp1S9pgVC2xsBARUanefvttJCYmwt7eHgBw7do19OjRA3fu3JE4GVU3LCxERPRa9erVw6FDh2BnZwcA+Ouvv9CrVy88evRI2mBUrbCwEBHRGzVq1AiHDh2ClZUVAODMmTPw9PTE48ePJU5G1QULCxERlck777yDQ4cOoX79+gCAX3/9FQMHDsSzZ88kTkbVAQsLERGV2XvvvYfExES8/fbbAIDDhw9j+PDhKCgokDYY6T0WFiIi0kjbtm1x8OBB1KxZEwCwf/9+jB49GiqVSuJkpM9YWIiISGPOzs7Yt28fFAoFACAmJgZTpkyBIAgSJyN9xcJCRETl0rVrV2zfvh2GhoYAgPDwcHz22WcsLVQpWFiIiKjc+vXrh82bN0MmkwEAgoODsWjRIolTkT5iYSEion/F29sbYWFh4voXX3yB77//XsJEpI9YWIiI6F+bOHEigoODxXV/f3/89NNPEiYifcPCQkREFWLmzJmYP3++uD5+/Hjs2rVLwkSkT1hYiIiownz11Vf45JNPAABFRUUYMWIEDh06JHEq0gcsLEREVGFkMhlWrVqF0aNHAwDy8/Ph5eWFX3/9VeJkpOvKVVhCQkJga2sLExMTODk5ITk5udRtjx07hk6dOqFOnTowNTVFixYtsHLlyhLb7dixAy1btoRCoUDLli15GZGISEcZGBhg/fr18PLyAgA8efIEffr0wblz56QNRjpN48ISGxuL6dOnIyAgAGlpaXBzc4OnpycyMjJeub2ZmRmmTZuGo0ePIj09HYGBgQgMDFS7o/zEiRPw9vaGj48P/vjjD/j4+GD48OE4efJk+Y+MiIgkY2hoiJiYGHTv3h0A8PDhQ3h4eODy5csSJyNdJRM0nOHH2dkZjo6OCA0NFcfs7e3h5eWFoKCgMu1j8ODBMDMzQ2RkJIDin8Tl5OQgPj5e3KZ3796oVasWoqOjy7TPnJwcWFhYIDs7G+bm5hocERERVZbHjx+jR48e4l9AbW1tcezYMTRq1EjiZKQtyvr5rdEVlvz8fKSmpsLDw0Nt3MPDAykpKWXaR1paGlJSUuDu7i6OnThxosQ+e/Xq9dp95uXlIScnR20hIiLtUrNmTcTFxaFVq1YAgKtXr6Jnz564f/++xMlI12hUWO7duweVSgVLS0u1cUtLS2RlZb32vVZWVlAoFGjfvj38/PwwceJE8bWsrCyN9xkUFAQLCwtxsba21uRQiIioitSuXRuJiYmwtbUFAJw/fx59+vRBbm6uxMlIl5TrptsXUzC/IAhCibGXJScn4/Tp01izZg1WrVpV4qseTfc5b948ZGdni8uNGzc0PAoiIqoqjRo1glKpRIMGDQAAp06dwqBBg5CXlydxMtIVhppsXLduXcjl8hJXPu7cuVPiCsnLXjTr1q1b459//sGCBQswcuRIAECDBg003qdCoRCfEkpERNrPzs4OiYmJ6NKlCx49eoSff/4ZH330EWJjYyGXy6WOR1pOoyssxsbGcHJyglKpVBtXKpXo2LFjmfcjCIJaq3Z1dS2xz8TERI32SURE2q9169aIi4tDjRo1ABRPaTF58mQ+4ZneSKMrLEDx1Ms+Pj5o3749XF1dERYWhoyMDPj6+gIo/qrm1q1b2LRpEwBg9erVaNKkCVq0aAGgeF6W5cuXizMhAsXPnOjSpQu+/fZbDBw4EHv27MGhQ4dw7NixijhGIiLSIq6urti5cyf69++PgoICrF+/HnXq1MG3334rdTTSYhoXFm9vb9y/fx8LFy5EZmYmHBwcEBcXBxsbGwBAZmam2pwsRUVFmDdvHq5evQpDQ0PY2dlhyZIlmDx5srhNx44dERMTg8DAQMyfPx92dnaIjY2Fs7NzBRwiERFpm169eiEyMhIjR46EIAhYunQpateujf/5n/+ROhppKY3nYdFWnIeFiEj3rFmzBlOmTBHX161bhwkTJkiYiKpapczDQkREVJF8fX2xaNEicX3SpEl8NAu9EgsLERFJ6vPPP8eMGTMA/O8Tno8cOSJxKtI2LCxERCQpmUyG5cuXqz3hecCAAUhNTZU4GWkTFhYiIpKcgYEB1q1bh/79+wMofgZR7969cfHiRYmTkbZgYSEiIq1gZGSE2NhYuLm5ASh+HEzPnj1x69YtiZORNmBhISIirWFqaop9+/ahbdu2AICMjAx4eHjgwYMHEicjqbGwEBGRVrGwsMDBgwfRtGlTAMUPS+zXrx+ePHkicTKSEgsLERFpnQYNGiAxMVF8ptyJEycwbNgwFBQUSJyMpMLCQkREWsnOzg4JCQmwsLAAAMTHx2Ps2LEoKiqSOBlJgYWFiIi0Vtu2bbFv3z6YmJgAAKKiojBz5kw+LLEaYmEhIiKt5ubmhtjYWMjlcgDAd999hyVLlkiciqoaCwsREWm9AQMGIDw8XFz//PPPsW7dOgkTUVVjYSEiIp0wbtw4tSsrkydPxu7du6ULRFWKhYWIiHTGnDlzMHPmTAD/+9yho0ePSpyKqgILCxER6QyZTIZly5Zh1KhRAIC8vDwMGDAAZ8+elTgZVTYWFiIi0ikGBgaIiIiAp6cnACA7Oxu9e/fG1atXJU5GlYmFhYiIdI6RkRG2bdsGZ2dnAEBmZiZ69eqFu3fvSpyMKgsLCxER6SQzMzMcOHAALVq0AABcunQJffr0wePHjyVORpWBhYWIiHRWnTp1kJCQgMaNGwMATp8+jcGDByM/P1/iZFTRWFiIiEinNWnSBAkJCXj77bcBAEqlEuPGjeMU/nqGhYWIiHReq1atsH//frUp/GfPns0p/PUICwsREemFTp06ITY2FgYGxR9tK1euxPLlyyVORRWFhYWIiPTGgAEDsHbtWnF9zpw52LRpk4SJqKKwsBARkV6ZOHEivv76a3F9/PjxiI+PlzARVQQWFiIi0jsBAQHw8/MDAKhUKgwdOhSnTp2SOBX9GywsRESkd2QyGb777jsMHToUAPD06VP07dsXFy9elDgZlRcLCxER6SW5XI7IyEi4u7sDAO7du4devXohMzNT4mRUHiwsRESkt0xMTLBnzx60adMGAHDt2jV4enoiOztb4mSkKRYWIiLSaxYWFoiPj4eNjQ0A4I8//sDgwYORl5cncTLSBAsLERHpvUaNGiEhIQF16tQBABw+fBhjxozhbLg6hIWFiIiqhffeew/79++HqakpACA2NhazZs3ibLg6goWFiIiqDRcXF2zduhVyuRwAsGrVKgQHB0ucisqiXIUlJCQEtra2MDExgZOTE5KTk0vddufOnejZsyfq1asHc3NzuLq6IiEhocR2q1atwnvvvQdTU1NYW1tjxowZeP78eXniERERlapfv34ICwsT1z/77DNs3rxZwkRUFhoXltjYWEyfPh0BAQFIS0uDm5sbPD09kZGR8crtjx49ip49eyIuLg6pqano1q0b+vfvj7S0NHGbLVu2YO7cufjyyy+Rnp6O9evXIzY2FvPmzSv/kREREZVi/PjxarPhjhs3DomJiRImojeRCRp+eefs7AxHR0eEhoaKY/b29vDy8kJQUFCZ9tGqVSt4e3vjiy++AABMmzYN6enp+Pnnn8VtZs2ahVOnTr326s3/lZOTAwsLC2RnZ8Pc3FyDIyIioupIEARMnToVa9asAQDUrFkTSUlJcHR0lDhZ9VLWz2+NrrDk5+cjNTUVHh4eauMeHh5ISUkp0z6KioqQm5uL2rVri2OdO3dGamqqOG3ylStXEBcXh759+5a6n7y8POTk5KgtREREZSWTyfDjjz9i0KBBAIDHjx+jT58+uHLlisTJ6FU0Kiz37t2DSqWCpaWl2rilpSWysrLKtI/g4GA8efIEw4cPF8dGjBiBr7/+Gp07d4aRkRHs7OzQrVs3zJ07t9T9BAUFwcLCQlysra01ORQiIiLI5XJs2bIFnTp1AgD8888/6N27N+7evStxMnpZuW66lclkauuCIJQYe5Xo6GgsWLAAsbGxqF+/vjj+yy+/4JtvvkFISAh+//137Ny5E/v371f7fvFl8+bNQ3Z2trjcuHGjPIdCRETVnKmpKfbu3Qt7e3sAwKVLl9CvXz88efJE4mT0fxlqsnHdunUhl8tLXE25c+dOiasuL4uNjcWECROwbds29OjRQ+21+fPnw8fHBxMnTgQAtG7dGk+ePMGkSZMQEBAAA4OSvUqhUEChUGgSn4iI6JVq166NgwcPwtXVFbdv38apU6fg7e2N3bt3w9BQo49KqiQaXWExNjaGk5MTlEql2rhSqUTHjh1LfV90dDTGjh2LqKioV96X8vTp0xKlRC6XQxAETuhDRERVokmTJoiPjxdv/Dxw4ACmTJnCzyEtofFXQjNnzsS6desQERGB9PR0zJgxAxkZGfD19QVQ/FXN6NGjxe2jo6MxevRoBAcHw8XFBVlZWcjKylJ78FT//v0RGhqKmJgYXL16FUqlEvPnz8eAAQPEyX2IiIgqW5s2bbB7924YGxsDANatW4eFCxdKnIoAAEI5rF69WrCxsRGMjY0FR0dHISkpSXxtzJgxgru7u7ju7u4uACixjBkzRtymoKBAWLBggWBnZyeYmJgI1tbWwtSpU4WHDx+WOVN2drYAQMjOzi7PIREREYliYmLUPrPCw8OljqS3yvr5rfE8LNqK87AQEVFFWrlyJWbOnAmg+DaFPXv2vHa6DSqfSpmHhYiIqLqYMWOGWFhUKhWGDx8uzhdGVY+FhYiIqBTLli2Dt7c3gOIfiPTt2xd///23xKmqJxYWIiKiUhgYGOCnn35C165dARRPoNq7d2/cuXNH2mDVEAsLERHRaygUCuzatQsODg4AgMuXL3NiOQmwsBAREb3B22+/jfj4eFhZWQEAfvvtNwwfPhyFhYUSJ6s+WFiIiIjKwMrKCvHx8bCwsAAAxMXFwdfXlxPLVREWFiIiojJycHBQm1hu/fr1nFiuirCwEBERaaBr167YtGmTuL5gwQJERERImKh6YGEhIiLSkLe3N5YvXy6uT5o0CfHx8RIm0n8sLEREROUwc+ZM+Pv7AyieWG7YsGE4ffq0xKn0FwsLERFROchkMqxYsQJDhw4FADx58gR9+/bFlStXJE6mn1hYiIiIysnAwACRkZHo3LkzAODOnTvw9PTE/fv3JU6mf1hYiIiI/gUTExPs2bMH9vb2AICLFy9iwIABePbsmcTJ9AsLCxER0b9Uu3ZtxMfHo0GDBgCAlJQUfPTRR1CpVBIn0x8sLERERBXAxsYGcXFxqFmzJgBg165dmDFjBieWqyAsLERERBWkXbt22LFjBwwNDQEAP/zwA1asWCFxKv3AwkJERFSBPDw8EB4eLq7Pnj0bMTExEibSDywsREREFWzs2LFqU/aPGTMGSUlJEibSfSwsRERElSAwMBATJ04EAOTn58PLywvnz5+XOJXuYmEhIiKqBDKZDKGhofD09AQAPHr0CJ6enrh9+7bEyXQTCwsREVElMTQ0xNatW+Ho6AgAyMjIQN++fZGbmytxMt3DwkJERFSJatasiQMHDsDGxgYAcObMGQwdOhQFBQUSJ9MtLCxERESVrEGDBoiPj0etWrUAAImJiZg8eTLnaNEACwsREVEVsLe3x549e6BQKAAAGzZsUPslEb0eCwsREVEVcXNzw6ZNm8T1BQsWYMOGDRIm0h0sLERERFVo+PDhWL58ubg+adIkJCYmSphIN7CwEBERVbGZM2fik08+AQAUFhZiyJAhOHPmjLShtBwLCxERURWTyWRYuXIlBg0aBAB4/Pgx+vTpg4yMDImTaS8WFiIiIgnI5XJs2bIFLi4uAIDMzEz06dMHjx49kjaYlmJhISIikoipqSn27t2Ld999FwDw3//+F4MHD0ZeXp7EybQPCwsREZGE6tWrh/j4eNStWxcAcOTIEUyYMIFztLyEhYWIiEhi7777Lvbt2wdTU1MAwJYtWxAQECBxKu1SrsISEhICW1tbmJiYwMnJCcnJyaVuu3PnTvTs2RP16tWDubk5XF1dkZCQUGK7R48ewc/PDw0bNoSJiQns7e0RFxdXnnhEREQ6x8XFBVFRUZDJZACAoKAghIWFSZxKe2hcWGJjYzF9+nQEBAQgLS0Nbm5u8PT0LPXO5qNHj6Jnz56Ii4tDamoqunXrhv79+yMtLU3cJj8/Hz179sS1a9ewfft2XLhwAeHh4WjcuHH5j4yIiEjHeHl54bvvvhPXp06dyr+8/38yQcMvyZydneHo6IjQ0FBxzN7eHl5eXggKCirTPlq1agVvb2988cUXAIA1a9Zg2bJl+Ouvv2BkZKRJHFFOTg4sLCyQnZ0Nc3Pzcu2DiIhIG8yePRvBwcEAADMzMxw9elR84rO+Kevnt0ZXWPLz85GamgoPDw+1cQ8PD6SkpJRpH0VFRcjNzUXt2rXFsb1798LV1RV+fn6wtLSEg4MDFi9eDJVKVep+8vLykJOTo7YQERHpg6VLl2Lo0KEAgCdPnqBv3764du2atKEkplFhuXfvHlQqFSwtLdXGLS0tkZWVVaZ9BAcH48mTJxg+fLg4duXKFWzfvh0qlQpxcXEIDAxEcHAwvvnmm1L3ExQUBAsLC3GxtrbW5FCIiIi0loGBASIjI9GpUycAQFZWFvr06YOHDx9KnEw65brp9sUNQS8IglBi7FWio6OxYMECxMbGon79+uJ4UVER6tevj7CwMDg5OWHEiBEICAhQ+9rpZfPmzUN2dra43LhxozyHQkREpJVMTEywZ88eNG/eHACQnp6OQYMGVds5WjQqLHXr1oVcLi9xNeXOnTslrrq8LDY2FhMmTMDWrVvRo0cPtdcaNmyI5s2bQy6Xi2P29vbIyspCfn7+K/enUChgbm6uthAREemTOnXqID4+HvXq1QMAJCUlYfz48SgqKpI4WdXTqLAYGxvDyckJSqVSbVypVKJjx46lvi86Ohpjx45FVFQU+vbtW+L1Tp064e+//1b7H+DixYto2LAhjI2NNYlIRESkV5o2bYr9+/eLc7RERUVh/vz5Eqeqehp/JTRz5kysW7cOERERSE9Px4wZM5CRkQFfX18AxV/VjB49Wtw+Ojoao0ePRnBwMFxcXJCVlYWsrCxkZ2eL20yZMgX379+Hv78/Ll68iAMHDmDx4sXw8/OrgEMkIiLSbR06dEBMTAwMDIo/thcvXlz95mgRymH16tWCjY2NYGxsLDg6OgpJSUnia2PGjBHc3d3FdXd3dwFAiWXMmDFq+0xJSRGcnZ0FhUIhNG3aVPjmm2+EwsLCMmfKzs4WAAjZ2dnlOSQiIiKt9+OPP4qfo3K5XDhw4IDUkf61sn5+azwPi7biPCxERFQdfPbZZ1i+fDmA4jlakpKS4OTkJHGq8quUeViIiIhIWt9++y2GDRsGoHiOln79+uH69esSp6p8LCxEREQ6xMDAAJs2bSoxR8ujR4+kDVbJWFiIiIh0zIs5Wpo1awYAOH/+PAYPHlzqVCD6gIWFiIhIB708R8uRI0cwceJE6MmtqSWwsBAREekoOzs77N27FyYmJgCAyMhI8cHC+oaFhYiISIe5uLggKipKfETOokWLEBERIXGqisfCQkREpOMGDRqElStXiuuTJk1CQkKChIkqHgsLERGRHvD394e/vz8AQKVSYejQofjjjz8kTlVxWFiIiIj0RHBwMAYNGgQAePz4Mfr27YubN29KnKpisLAQERHpCblcjs2bN8PZ2RkAcOvWLfTp00ft+X26ioWFiIhIj9SoUQN79+5F06ZNAQDnzp3DsGHDUFBQIHGyf4eFhYiISM/Ur18f8fHxqF27NgBAqVRi8uTJOj1HCwsLERGRHmrevDn27NkDhUIBANiwYQMWLVokcaryY2EhIiLSU507d0ZkZKS4/sUXX6it6xIWFiIiIj02bNgwLF26VFyfMGECDh8+LGGi8mFhISIi0nOzZ8/GlClTAAAFBQUYPHgw/vvf/0qcSjMsLERERHpOJpPh+++/R79+/QAA2dnZ6NOnDzIzMyVOVnYsLERERNWAoaEhYmJi4OTkBADIyMhAv3798PjxY4mTlQ0LCxERUTVhZmaGffv2oUmTJgCA33//HSNGjEBhYaHEyd6MhYWIiKgaadiwIeLi4mBhYQEAOHDgAD799FOtn6OFhYWIiKiaadWqFXbt2gUjIyMAQGhoKJYvXy5xqtdjYSEiIqqGunXrhoiICHF9zpw52Lp1q4SJXo+FhYiIqJoaNWoUFi5cKK6PHj0ax48flzBR6VhYiIiIqrHAwECMHz8eAJCXl4cBAwbg4sWLEqcqiYWFiIioGpPJZFizZg169uwJAHjw4AE8PT1x9+5diZOpY2EhIiKq5oyMjLB9+3a0bt0aAHDlyhUMGDAAz549kzjZ/2JhISIiIpibmyMuLg6NGjUCAPz6668YNWoUVCqVxMmKsbAQERERAMDKygpxcXGoWbMmAGDnzp347LPPJE5VjIWFiIiIRG3btsX27dshl8sBACtXrsQPP/wgcSoWFiIiInpJr169sGbNGnHd398fe/bskTARCwsRERG9wsSJE/H5558DAARBwMiRI3Hq1CnJ8rCwEBER0SstWrQIH374IQDg2bNn8Pb2RkFBgSRZylVYQkJCYGtrCxMTEzg5OSE5ObnUbXfu3ImePXuiXr16MDc3h6urKxISEkrdPiYmBjKZDF5eXuWJRkRERBVEJpMhIiIC7u7uqF+/PmJjY8XnD1U1jQtLbGwspk+fjoCAAKSlpcHNzQ2enp7IyMh45fZHjx5Fz549ERcXh9TUVHTr1g39+/dHWlpaiW2vX7+O2bNnw83NTfMjISIiogqnUCiwa9cu/Prrr+jQoYNkOWSChs+TdnZ2hqOjI0JDQ8Uxe3t7eHl5ISgoqEz7aNWqFby9vfHFF1+IYyqVCu7u7hg3bhySk5Px6NEj7N69u8y5cnJyYGFhgezsbJibm5f5fURERCSdsn5+a3SFJT8/H6mpqfDw8FAb9/DwQEpKSpn2UVRUhNzcXNSuXVttfOHChahXrx4mTJhQpv3k5eUhJydHbSEiIiL9pFFhuXfvHlQqFSwtLdXGLS0tkZWVVaZ9BAcH48mTJxg+fLg4dvz4caxfvx7h4eFlzhIUFAQLCwtxsba2LvN7iYiISLeU66ZbmUymti4IQomxV4mOjsaCBQsQGxuL+vXrAwByc3MxatQohIeHo27dumXOMG/ePGRnZ4vLjRs3NDsIIiIi0hmGmmxct25dyOXyEldT7ty5U+Kqy8tiY2MxYcIEbNu2DT169BDHL1++jGvXrqF///7iWFFRUXE4Q0NcuHABdnZ2JfanUCigUCg0iU9EREQ6SqMrLMbGxnBycoJSqVQbVyqV6NixY6nvi46OxtixYxEVFYW+ffuqvdaiRQucO3cOZ86cEZcBAwagW7duOHPmDL/qISIiIs2usADAzJkz4ePjg/bt28PV1RVhYWHIyMiAr68vgOKvam7duoVNmzYBKC4ro0ePxnfffQcXFxfx6oypqSksLCxgYmICBwcHtX/H22+/DQAlxomIiKh60riweHt74/79+1i4cCEyMzPh4OCAuLg42NjYAAAyMzPV5mRZu3YtCgsL4efnBz8/P3F8zJgx2Lhx478/AiIiItJ7Gs/Doq04DwsREZHuqZR5WIiIiIikwMJCREREWo+FhYiIiLQeCwsRERFpPY1/JaStXtw7zGcKERER6Y4Xn9tv+g2Q3hSW3NxcAOBEc0RERDooNzcXFhYWpb6uNz9rLioqwu3bt/HWW2+V6blGZZWTkwNra2vcuHGDP5euRDzPVYfnumrwPFcNnueqUZnnWRAE5ObmolGjRjAwKP1OFb25wmJgYAArK6tK27+5uTn/z1AFeJ6rDs911eB5rho8z1Wjss7z666svMCbbomIiEjrsbAQERGR1mNheQOFQoEvv/wSCoVC6ih6jee56vBcVw2e56rB81w1tOE8681Nt0RERKS/eIWFiIiItB4LCxEREWk9FhYiIiLSeiwsREREpPVYWACEhITA1tYWJiYmcHJyQnJy8mu3T0pKgpOTE0xMTNC0aVOsWbOmipLqNk3O886dO9GzZ0/Uq1cP5ubmcHV1RUJCQhWm1V2a/nl+4fjx4zA0NMT7779fuQH1iKbnOi8vDwEBAbCxsYFCoYCdnR0iIiKqKK3u0vQ8b9myBW3btkWNGjXQsGFDjBs3Dvfv36+itLrp6NGj6N+/Pxo1agSZTIbdu3e/8T1V/lkoVHMxMTGCkZGREB4eLpw/f17w9/cXzMzMhOvXr79y+ytXrgg1atQQ/P39hfPnzwvh4eGCkZGRsH379ipOrls0Pc/+/v7Ct99+K5w6dUq4ePGiMG/ePMHIyEj4/fffqzi5btH0PL/w6NEjoWnTpoKHh4fQtm3bqgmr48pzrgcMGCA4OzsLSqVSuHr1qnDy5Enh+PHjVZha92h6npOTkwUDAwPhu+++E65cuSIkJycLrVq1Ery8vKo4uW6Ji4sTAgIChB07dggAhF27dr12eyk+C6t9YenQoYPg6+urNtaiRQth7ty5r9x+zpw5QosWLdTGJk+eLLi4uFRaRn2g6Xl+lZYtWwpfffVVRUfTK+U9z97e3kJgYKDw5ZdfsrCUkabnOj4+XrCwsBDu379fFfH0hqbnedmyZULTpk3Vxr7//nvBysqq0jLqm7IUFik+C6v1V0L5+flITU2Fh4eH2riHhwdSUlJe+Z4TJ06U2L5Xr144ffo0CgoKKi2rLivPeX5ZUVERcnNzUbt27cqIqBfKe543bNiAy5cv48svv6zsiHqjPOd67969aN++PZYuXYrGjRujefPmmD17Np49e1YVkXVSec5zx44dcfPmTcTFxUEQBPzzzz/Yvn07+vbtWxWRqw0pPgv15uGH5XHv3j2oVCpYWlqqjVtaWiIrK+uV78nKynrl9oWFhbh37x4aNmxYaXl1VXnO88uCg4Px5MkTDB8+vDIi6oXynOdLly5h7ty5SE5OhqFhtf7PgUbKc66vXLmCY8eOwcTEBLt27cK9e/cwdepUPHjwgPexlKI857ljx47YsmULvL298fz5cxQWFmLAgAH44YcfqiJytSHFZ2G1vsLygkwmU1sXBKHE2Ju2f9U4qdP0PL8QHR2NBQsWIDY2FvXr16+seHqjrOdZpVLhww8/xFdffYXmzZtXVTy9osmf6aKiIshkMmzZsgUdOnRAnz59sGLFCmzcuJFXWd5Ak/N8/vx5fPrpp/jiiy+QmpqKgwcP4urVq/D19a2KqNVKVX8WVuu/UtWtWxdyubxEU79z506J5vhCgwYNXrm9oaEh6tSpU2lZdVl5zvMLsbGxmDBhArZt24YePXpUZkydp+l5zs3NxenTp5GWloZp06YBKP5QFQQBhoaGSExMxH/+858qya5ryvNnumHDhmjcuDEsLCzEMXt7ewiCgJs3b6JZs2aVmlkXlec8BwUFoVOnTvjss88AAG3atIGZmRnc3NywaNEiXgWvIFJ8FlbrKyzGxsZwcnKCUqlUG1cqlejYseMr3+Pq6lpi+8TERLRv3x5GRkaVllWXlec8A8VXVsaOHYuoqCh+/1wGmp5nc3NznDt3DmfOnBEXX19fvPfeezhz5gycnZ2rKrrOKc+f6U6dOuH27dt4/PixOHbx4kUYGBjAysqqUvPqqvKc56dPn8LAQP2jTS6XA/jfKwD070nyWVhpt/PqiBc/mVu/fr1w/vx5Yfr06YKZmZlw7do1QRAEYe7cuYKPj4+4/Yufcs2YMUM4f/68sH79ev6suQw0Pc9RUVGCoaGhsHr1aiEzM1NcHj16JNUh6ARNz/PL+CuhstP0XOfm5gpWVlbC0KFDhf/+979CUlKS0KxZM2HixIlSHYJO0PQ8b9iwQTA0NBRCQkKEy5cvC8eOHRPat28vdOjQQapD0Am5ublCWlqakJaWJgAQVqxYIaSlpYk/H9eGz8JqX1gEQRBWr14t2NjYCMbGxoKjo6OQlJQkvjZmzBjB3d1dbftffvlFaNeunWBsbCy88847QmhoaBUn1k2anGd3d3cBQIllzJgxVR9cx2j65/n/YmHRjKbnOj09XejRo4dgamoqWFlZCTNnzhSePn1axal1j6bn+fvvvxdatmwpmJqaCg0bNhQ++ugj4ebNm1WcWrccOXLktf/N1YbPQpkg8BoZERERabdqfQ8LERER6QYWFiIiItJ6LCxERESk9VhYiIiISOuxsBAREZHWY2EhIiIircfCQkRERFqPhYWIiIi0HgsLERERaT0WFiIiItJ6LCxERESk9VhYiIiISOv9P6ifLJYGXAS8AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Overlay a line plot representing the normal distribution's probability density function (PDF)\n",
    "xmin, xmax = plt.xlim()\n",
    "x = np.linspace(xmin, xmax, 100)\n",
    "p = norm.pdf(x, 0, 1)  # PDF of standard normal distribution with mean=0 and std=1\n",
    "plt.plot(x, p, 'k', linewidth=2, label='PDF')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "2febfabe-1bbc-40ab-b7d9-49d2b2d7174b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Frequency/Probability')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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fCM/P9+QZKSnpxv5+flNtzJw1vHb44KQYRjGqlWrjPDwcMPPz8+Iiooydu/e3fTZI488Ytxxxx1W/f/6178at956q+Hn52f069fPWLNmjYsr9ly2jMUdd9xhSGr2euSRR1xfuIey9e/GPyMIOZatY1FQUGCMHTvW6NSpkxEaGmqkpqYa58+fd3HVnsnWsVi5cqUxaNAgo1OnTkavXr2MBx980Dh16pSLq/Y8u3btuuoxwFnHb4thMJcHAADMyaPWCAEAANiCIAQAAEyLIAQAAEyLIAQAAEyLIAQAAEyLIAQAAEyLIAQAAEyLIATAI9x5552aO3euu8sA0MEQhAC43aRJk674gN0DBw7IYrHo0KFDLq4KgBkQhAC4XWJionbu3KkTJ040+ywjI0NDhw5VVFSUGyoD4OkIQgDc7l//9V8VHBysjRs3WrWfP39eWVlZmjJlin79618rNDRUnTt31k033aQtW7ZcdZ8Wi0UffvihVdu1115r9R2nT59WfHy8fvGLX6hbt26aPHmyvvnmG8f8KAAdAkEIgNv5+PgoISFBGzdu1D8//nDr1q2qq6vT7NmzFR0drb/85S/66quv9Jvf/EYPP/ywPv/8c7u/8/z58xo9erSuueYa7dmzR3v37tU111yju+++W3V1dY74WQA6AIIQgHZh1qxZ+uabb/TXv/61qS0jI0NTp05Vnz59tGDBAg0dOlT9+/fX7373O40fP15bt261+/veeecdeXl5af369brpppsUGRmpzMxMlZSUWNUAwLP5uLsAAJCkG2+8UbGxscrIyNDo0aNVWFio3Nxc7dixQ/X19XrxxReVlZWl06dPq7a2VrW1terSpYvd33fw4EH9/e9/V9euXa3aL1y4oMLCwrb+HAAdBEEIQLuRmJioOXPmaNWqVcrMzFR4eLjuuusuvfLKK/rjH/+oFStW6KabblKXLl00d+7cq57CslgsVqfZJOnixYtNf25oaFB0dLQ2b97cbNsePXo47kcBaNcIQgDajWnTpiklJUVvv/223nrrLT366KOyWCzKzc3V5MmT9dBDD0m6HGKOHz+uyMjIK+6rR48eKi0tbXp//PhxnT9/vul9VFSUsrKyFBwcrMDAQOf9KADtGmuEALQb11xzjeLj4/X000/rzJkzmjFjhiRpwIABysnJ0f79+1VQUKDHHntMZWVlV93XmDFj9MYbb+jQoUPKy8tTUlKSfH19mz5/8MEH1b17d02ePFm5ubkqLi7W7t27lZKSolOnTjnzZwJoRwhCANqVxMREff/99xo7dqz69u0rSXr22WcVFRWl8ePH684771TPnj01ZcqUq+5n+fLlCgsL0+23367p06drwYIF6ty5c9PnnTt31p49e9S3b19NnTpVkZGRmjVrln788UdmiAATsRg/PYkOAABgEswIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0yIIAQAA0/p/E0CsrHxdUycAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Label the axes\n",
    "plt.xlabel('Value')\n",
    "plt.ylabel('Frequency/Probability')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3a128ff0-c8cd-4e79-afaa-c9fa0734bc61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Histogram with PDF Overlay')"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAi4AAAGxCAYAAABFkj3UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8o6BhiAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAscElEQVR4nO3de1xVdb7/8ffmtkENKk0URUQzxRw14WhSpnnBtPTYo450mbykzdDNC9ZJokmxOkw2drp5GRO1GutQmeYUlVhm5KXUwZqSxkoTHSECH4KlIcL394cP9s/dBmUjF7/wej4e6+Fjf/mutT57fzeuN+u79toOY4wRAACABXwauwAAAICaIrgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguMA6K1eulMPh0I4dO6r8+Q033KDOnTu7tXXu3FmTJk3yaj9btmzR3LlzdeTIkdoV2sz99jU/dOiQ5s6dq127dnn0nTRpklq1alXrfQ0ZMkQOh8O1BAUFqU+fPnrmmWdUUVHhtp/T+7Vs2VKdO3fW2LFjtWLFCpWWlp5126cvX3311VlrKyoqUlJSknr27KkWLVooODhYV155pRYuXKiysrJaP+e64HA4NHfu3EatAfCWX2MXADSENWvWKDg42Kt1tmzZopSUFE2aNEkXXnhh/RTWhP32NT906JBSUlLUuXNn9e3bt87316VLF61atUqSVFBQoCVLlmjmzJnKy8vTk08+6eoXFBSkjz76SJJ0/PhxHThwQO+9957uuusuLViwQO+//746duxY7bZP17Vr1zPW9M033yguLk4///yzZs2apdjYWB0/flzvvPOOpk+frjfeeEMZGRlq0aLFuT59oNkguKBZuOKKKxq7BK+VlZXJ4XDIz8/OX9OGfs2DgoJ05ZVXuh6PGjVKPXr00AsvvKDHH39c/v7+kiQfHx+3fpI0YcIETZ48WTfccINuvvlmbdu27Yzbrony8nLddNNNKikp0eeff67LLrvM9bPRo0dr8ODBuuWWW5SYmKglS5Z4+3RrzRijX3/9VUFBQQ22T6AuMVWEZuG30xYVFRV6/PHH1b17dwUFBenCCy9U79699eyzz0qS5s6dqwcffFCSFBkZ6Zoa+Pjjj13rz58/Xz169JDT6VTbtm01YcIEHTx40G2/xhj9z//8jyIiIhQYGKiYmBhlZmZqyJAhGjJkiKvfxx9/LIfDoVdeeUWzZs1Shw4d5HQ69d133+mnn37SPffco549e6pVq1Zq27athg4dqqysLLd9/fDDD3I4HHrqqaf05JNPqnPnzgoKCtKQIUO0Z88elZWVafbs2QoLC1NISIhuvPFGFRQUnPF1e/fdd+VwOLR9+3ZX2+rVq+VwOHT99de79e3du7duuummKl/zjz/+WP/xH/8hSZo8ebLr9fztNMV3332n0aNHq1WrVgoPD9esWbOqnL6pCX9/f0VHR+vYsWP66aefzto/Li5Od911lz777DN98skntdrn6dasWaPdu3dr9uzZbqGlUnx8vOLi4pSWlqb8/HyVlZWpbdu2uuOOOzz6HjlyREFBQUpMTHS1lZSU6IEHHlBkZKQCAgLUoUMHzZgxQ7/88ovbug6HQ/fdd5+WLFmiqKgoOZ1OvfTSS1XWXJP3mjFG3bp108iRIz3W//nnnxUSEqJ77723xq8T4C2CC6xVXl6ukydPeiw1+cLz+fPna+7cubr11lv17rvvKj09XVOmTHFdzzJ16lTdf//9kqS33npLW7du1datW9WvXz9J0t13362HHnpII0aM0Lp16/TYY4/p/fffV2xsrAoLC137SU5OVnJysq677jq9/fbbSkhI0NSpU7Vnz54q60pKSlJubq6WLFmiv//972rbtq0OHz4sSZozZ47effddrVixQl26dNGQIUNcQep0Cxcu1ObNm7Vw4UItW7ZM33zzjcaMGaMpU6bop59+0vLlyzV//nxt2LBBU6dOPePrNHjwYPn7+2vDhg2utg0bNigoKEibNm1yXaNRUFCgr776SsOHD69yO/369dOKFSskSY888ojr9Tx9/2VlZRo7dqyGDRumt99+W3feeaf+93//122ax1vff/+9/Pz8dNFFF9Wo/9ixYyWpyuDy2/fZ6dfOVCUzM1OSNG7cuGr7jBs3TidPntTHH38sf39//f73v9fq1atVUlLi1u+1117Tr7/+qsmTJ0uSjh07psGDB+ull17StGnT9N577+mhhx7SypUrNXbsWI/fgbVr12rx4sV69NFH9cEHH2jQoEFV1lOT95rD4dD999+vzMxMffvtt27rv/zyyyopKSG4oH4ZwDIrVqwwks64REREuK0TERFhJk6c6Hp8ww03mL59+55xP0899ZSRZPbt2+fWnpOTYySZe+65x639s88+M5LMww8/bIwx5vDhw8bpdJr4+Hi3flu3bjWSzODBg11tGzduNJLMNddcc9bnf/LkSVNWVmaGDRtmbrzxRlf7vn37jCTTp08fU15e7mp/5plnjCQzduxYt+3MmDHDSDLFxcVn3N/VV19thg4d6np86aWXmgcffND4+PiYTZs2GWOMWbVqlZFk9uzZ4+r329d8+/btRpJZsWKFxz4mTpxoJJnXX3/drX306NGme/fuZ6zPGGMGDx5sLr/8clNWVmbKysrMoUOHzOzZs40k81//9V9u+2nZsmW126kc27vvvttt21W9x26//fYz1nTdddcZSebXX3+tts97771nJJknn3zSGGPMl19+aSSZpUuXuvXr37+/iY6Odj1OTU01Pj4+Zvv27W793nzzTSPJZGRkuNokmZCQEHP48GGP/Usyc+bMqba+6t5rJSUl5oILLjDTp09369+zZ09z7bXXVrs9oC5wxgXWevnll7V9+3aP5eqrrz7ruv3799cXX3yhe+65Rx988IHHX7hnsnHjRkny+JRS//79FRUVpQ8//FCStG3bNpWWlmr8+PFu/a688kqPTz1VOn2q5XRLlixRv379FBgYKD8/P/n7++vDDz9UTk6OR9/Ro0fLx+f//2pHRUVJksfUTmV7bm5uNc/0lGHDhmnz5s06fvy49u/fr++++0633HKL+vbt6zqrsGHDBnXq1EndunU747bOxOFwaMyYMW5tvXv31v79+2u0/tdffy1/f3/5+/srLCxMCxYs0O23364XX3yxxjWYas7Wde3a1eN99thjj9V4u2fbn8PhkCT97ne/U3R0tOvslCTl5OTo888/15133ulqe+edd9SrVy/17dvX7SzQyJEj3aY0Kw0dOrTGZ51q8l674IILNHnyZK1cudI1NfXRRx9p9+7duu+++2r1WgA1RXCBtaKiohQTE+OxhISEnHXdpKQk/eUvf9G2bds0atQotW7dWsOGDav2I9anKyoqkiS1b9/e42dhYWGun1f+Gxoa6tGvqrbqtvn000/r7rvv1oABA7R69Wpt27ZN27dv13XXXafjx4979L/44ovdHgcEBJyx/ddff62ylkrDhw9XaWmpPv30U2VmZqpNmza64oorNHz4cNcU0ocffljtNFFNtWjRQoGBgW5tTqfzrPVVqgwXO3bs0Fdf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Cy64oM62We/BpV27dsrPz3drKygokJ+fn9ut0U/ndDo9vuhLkoKDgwkuAABYpi4v86j3b4ceOHCgMjMz3drWr1+vmJiYKq9vAQAAqI7XweXnn3/Wrl27tGvXLkmnPu68a9cu5ebmSjo1zTNhwgRX/4SEBO3fv1+JiYnKycnR8uXLlZaWpgceeKBungEAAGg2vJ4q2rFjh6699lrX48prUSZOnKiVK1cqLy/PFWIkKTIyUhkZGZo5c6YWLlyosLAwPffcc7rpppvqoHwAANCcWHHL/5KSEoWEhKi4uJhrXAAAsER9HL/r/RoXAACAukJwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALBGrYLLokWLFBkZqcDAQEVHRysrK+uM/VetWqU+ffqoRYsWat++vSZPnqyioqJaFQwAAJovr4NLenq6ZsyYoeTkZGVnZ2vQoEEaNWqUcnNzq+z/6aefasKECZoyZYq+/vprvfHGG9q+fbumTp16zsUDAIDmxevg8vTTT2vKlCmaOnWqoqKi9Mwzzyg8PFyLFy+usv+2bdvUuXNnTZs2TZGRkbr66qv1xz/+UTt27Djn4gEAQPPiVXA5ceKEdu7cqbi4OLf2uLg4bdmypcp1YmNjdfDgQWVkZMgYox9//FFvvvmmrr/++mr3U1paqpKSErcFAADAq+BSWFio8vJyhYaGurWHhoYqPz+/ynViY2O1atUqxcfHKyAgQO3atdOFF16o559/vtr9pKam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quTkZEVERMjpdKpr165avnx5A1XbtHk7FqtWrVKfPn3UokULtW/fXpMnT1ZRUVEDVdt0ffLJJxozZozCwsLkcDi0du3as65TJ8ducx74v//7P+Pv729efPFFs3v3bjN9+nTTsmVLs3///ir7792717Ro0cJMnz7d7N6927z44ovG39/fvPnmmw1cedPj7VhMnz7dPPnkk+bzzz83e/bsMUlJScbf39/84x//aODKmx5vx6LSkSNHTJcuXUxcXJzp06dPwxTbxNVmLMaOHWsGDBhgMjMzzb59+8xnn31mNm/e3IBVN03ejkVWVpbx8fExzz77rNm7d6/Jysoyl19+uRk3blwDV970ZGRkmOTkZLN69WojyaxZs+aM/evq2H1eBJf+/fubhIQEt7YePXqY2bNnV9n/v//7v02PHj3c2v74xz+aK6+8st5qbC68HYuq9OzZ06SkpNR1ac1ObcciPj7ePPLII2bOnDkElzri7Vi89957JiQkxBQVFTVEec2Kt2Px1FNPmS5duri1Pffcc6Zjx471VmNzVJPgUlfH7kafKjpx4oR27typuLg4t/a4uDht2bKlynW2bt3q0X/kyJHasWOHysrK6q3Wpq42Y/FbFRUVOnr0aJ1+E2hzVNuxWLFihb7//nvNmTOnvktsNmozFuvWrVNMTIzmz5+vDh066LLLLtMDDzyg48ePN0TJTVZtxiI2NlYHDx5URkaGjDH68ccf9eabb+r6669viJJxmro6dnt9y/+6VlhYqPLyco9vlw4NDfX4VulK+fn5VfY/efKkCgsL1b59+3qrtymrzVj81oIFC/TLL79o/Pjx9VFis1Gbsfj22281e/ZsZWVlyc+v0X+1m4zajMXevXv16aefKjAwUGvWrFFhYaHuueceHT58mOtczkFtxiI2NlarVq1SfHy8fv31V508eVJjx47V888/3xAl4zR1dexu9DMulRwOh9tjY4xH29n6V9UO73k7FpVee+01zZ07V+np6Wrbtm19ldes1HQsysvLddtttyklJUWXXXZZQ5XXrHjze1FRUSGHw6FVq1apf//+Gj16tJ5++mmtXLmSsy51wJux2L17t6ZNm6ZHH31UO3fu1Pvvv699+/a5vhgYDasujt2N/mdZmzZt5Ovr65GWCwoKPJJZpXbt2lXZ38/PT61bt663Wpu62oxFpfT0dE2ZMkVvvPGGhg8fXp9lNgvejsXRo0e1Y8cOZWdn67777pN06uBpjJGfn5/Wr1+voUOHNkjtTU1tfi/at2+vDh06KCQkxNUWFRUlY4wOHjyobt261WvNTVVtxiI1NVVXXXWVHnzwQUlS79691bJlSw0aNEiPP/44Z+gbUF0duxv9jEtAQICio6OVmZnp1p6ZmanY2Ngq1xk4cKBH//Xr1ysmJkb+/v71VmtTV5uxkE6daZk0aZJeffVV5o3riLdjERwcrH/+85/atWuXa0lISFD37t21a9cuDRgwoKFKb3Jq83tx1VVX6dChQ/r5559dbXv27JGPj486duxYr/U2ZbUZi2PHjsnHx/1Q5+vrK+n//7WPhlFnx26vLuWtJ5Ufb0tLSzO7d+82M2bMMC1btjQ//PCDMcaY2bNnmzvuuMPVv/IjVTNnzjS7d+82aWlpfBy6jng7Fq+++qrx8/MzCxcuNHl5ea7lyJEjjfUUmgxvx+K3+FRR3fF2LI4ePWo6duxobr75ZvP111+bTZs2mW7dupmpU6c21lNoMrwdixUrVhg/Pz+zaNEi8/3335tPP/3UxMTEmP79+zfWU2gyjh49arKzs012draRZJ5++mmTnZ3t+mh6fR27z4vgYowxCxcuNBERESYgIMD069fPbNq0yfWziRMnmsGDB7v1//jjj80VV1xhAgICTOfOnc3ixYsbuOKmy5uxGDx4sJHksUycOLHhC2+CvP29OB3BpW55OxY5OTlm+PDhJigoyHTs2NEkJiaaY8eONXDVTZO3Y/Hcc8+Znj17mqCgINO+fXtz++23m4MHDzZw1U3Pxo0bz/j/f30dux3GcK4MAADYodGvcQEAAKgpggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWOP/AffH24v9EGeJAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Set the title of the plot\n",
    "plt.title('Histogram with PDF Overlay')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "c6546a8c-e035-44ef-a0fe-3c2e537856e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Histogram with PDF Overlay')"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAi4AAAGxCAYAAABFkj3UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8o6BhiAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAscElEQVR4nO3de1xVdb7/8ffmtkENKk0URUQzxRw14WhSpnnBtPTYo450mbykzdDNC9ZJokmxOkw2drp5GRO1GutQmeYUlVhm5KXUwZqSxkoTHSECH4KlIcL394cP9s/dBmUjF7/wej4e6+Fjf/mutT57fzeuN+u79toOY4wRAACABXwauwAAAICaIrgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguMA6K1eulMPh0I4dO6r8+Q033KDOnTu7tXXu3FmTJk3yaj9btmzR3LlzdeTIkdoV2sz99jU/dOiQ5s6dq127dnn0nTRpklq1alXrfQ0ZMkQOh8O1BAUFqU+fPnrmmWdUUVHhtp/T+7Vs2VKdO3fW2LFjtWLFCpWWlp5126cvX3311VlrKyoqUlJSknr27KkWLVooODhYV155pRYuXKiysrJaP+e64HA4NHfu3EatAfCWX2MXADSENWvWKDg42Kt1tmzZopSUFE2aNEkXXnhh/RTWhP32NT906JBSUlLUuXNn9e3bt87316VLF61atUqSVFBQoCVLlmjmzJnKy8vTk08+6eoXFBSkjz76SJJ0/PhxHThwQO+9957uuusuLViwQO+//746duxY7bZP17Vr1zPW9M033yguLk4///yzZs2apdjYWB0/flzvvPOOpk+frjfeeEMZGRlq0aLFuT59oNkguKBZuOKKKxq7BK+VlZXJ4XDIz8/OX9OGfs2DgoJ05ZVXuh6PGjVKPXr00AsvvKDHH39c/v7+kiQfHx+3fpI0YcIETZ48WTfccINuvvlmbdu27Yzbrony8nLddNNNKikp0eeff67LLrvM9bPRo0dr8ODBuuWWW5SYmKglS5Z4+3RrzRijX3/9VUFBQQ22T6AuMVWEZuG30xYVFRV6/PHH1b17dwUFBenCCy9U79699eyzz0qS5s6dqwcffFCSFBkZ6Zoa+Pjjj13rz58/Xz169JDT6VTbtm01YcIEHTx40G2/xhj9z//8jyIiIhQYGKiYmBhlZmZqyJAhGjJkiKvfxx9/LIfDoVdeeUWzZs1Shw4d5HQ69d133+mnn37SPffco549e6pVq1Zq27athg4dqqysLLd9/fDDD3I4HHrqqaf05JNPqnPnzgoKCtKQIUO0Z88elZWVafbs2QoLC1NISIhuvPFGFRQUnPF1e/fdd+VwOLR9+3ZX2+rVq+VwOHT99de79e3du7duuummKl/zjz/+WP/xH/8hSZo8ebLr9fztNMV3332n0aNHq1WrVgoPD9esWbOqnL6pCX9/f0VHR+vYsWP66aefzto/Li5Od911lz777DN98skntdrn6dasWaPdu3dr9uzZbqGlUnx8vOLi4pSWlqb8/HyVlZWpbdu2uuOOOzz6HjlyREFBQUpMTHS1lZSU6IEHHlBkZKQCAgLUoUMHzZgxQ7/88ovbug6HQ/fdd5+WLFmiqKgoOZ1OvfTSS1XWXJP3mjFG3bp108iRIz3W//nnnxUSEqJ77723xq8T4C2CC6xVXl6ukydPeiw1+cLz+fPna+7cubr11lv17rvvKj09XVOmTHFdzzJ16lTdf//9kqS33npLW7du1datW9WvXz9J0t13362HHnpII0aM0Lp16/TYY4/p/fffV2xsrAoLC137SU5OVnJysq677jq9/fbbSkhI0NSpU7Vnz54q60pKSlJubq6WLFmiv//972rbtq0OHz4sSZozZ47effddrVixQl26dNGQIUNcQep0Cxcu1ObNm7Vw4UItW7ZM33zzjcaMGaMpU6bop59+0vLlyzV//nxt2LBBU6dOPePrNHjwYPn7+2vDhg2utg0bNigoKEibNm1yXaNRUFCgr776SsOHD69yO/369dOKFSskSY888ojr9Tx9/2VlZRo7dqyGDRumt99+W3feeaf+93//122ax1vff/+9/Pz8dNFFF9Wo/9ixYyWpyuDy2/fZ6dfOVCUzM1OSNG7cuGr7jBs3TidPntTHH38sf39//f73v9fq1atVUlLi1u+1117Tr7/+qsmTJ0uSjh07psGDB+ull17StGnT9N577+mhhx7SypUrNXbsWI/fgbVr12rx4sV69NFH9cEHH2jQoEFV1lOT95rD4dD999+vzMxMffvtt27rv/zyyyopKSG4oH4ZwDIrVqwwks64REREuK0TERFhJk6c6Hp8ww03mL59+55xP0899ZSRZPbt2+fWnpOTYySZe+65x639s88+M5LMww8/bIwx5vDhw8bpdJr4+Hi3flu3bjWSzODBg11tGzduNJLMNddcc9bnf/LkSVNWVmaGDRtmbrzxRlf7vn37jCTTp08fU15e7mp/5plnjCQzduxYt+3MmDHDSDLFxcVn3N/VV19thg4d6np86aWXmgcffND4+PiYTZs2GWOMWbVqlZFk9uzZ4+r329d8+/btRpJZsWKFxz4mTpxoJJnXX3/drX306NGme/fuZ6zPGGMGDx5sLr/8clNWVmbKysrMoUOHzOzZs40k81//9V9u+2nZsmW126kc27vvvttt21W9x26//fYz1nTdddcZSebXX3+tts97771nJJknn3zSGGPMl19+aSSZpUuXuvXr37+/iY6Odj1OTU01Pj4+Zvv27W793nzzTSPJZGRkuNokmZCQEHP48GGP/Usyc+bMqba+6t5rJSUl5oILLjDTp09369+zZ09z7bXXVrs9oC5wxgXWevnll7V9+3aP5eqrrz7ruv3799cXX3yhe+65Rx988IHHX7hnsnHjRkny+JRS//79FRUVpQ8//FCStG3bNpWWlmr8+PFu/a688kqPTz1VOn2q5XRLlixRv379FBgYKD8/P/n7++vDDz9UTk6OR9/Ro0fLx+f//2pHRUVJksfUTmV7bm5uNc/0lGHDhmnz5s06fvy49u/fr++++0633HKL+vbt6zqrsGHDBnXq1EndunU747bOxOFwaMyYMW5tvXv31v79+2u0/tdffy1/f3/5+/srLCxMCxYs0O23364XX3yxxjWYas7Wde3a1eN99thjj9V4u2fbn8PhkCT97ne/U3R0tOvslCTl5OTo888/15133ulqe+edd9SrVy/17dvX7SzQyJEj3aY0Kw0dOrTGZ51q8l674IILNHnyZK1cudI1NfXRRx9p9+7duu+++2r1WgA1RXCBtaKiohQTE+OxhISEnHXdpKQk/eUvf9G2bds0atQotW7dWsOGDav2I9anKyoqkiS1b9/e42dhYWGun1f+Gxoa6tGvqrbqtvn000/r7rvv1oABA7R69Wpt27ZN27dv13XXXafjx4979L/44ovdHgcEBJyx/ddff62ylkrDhw9XaWmpPv30U2VmZqpNmza64oorNHz4cNcU0ocffljtNFFNtWjRQoGBgW5tTqfzrPVVqgwXO3bs0FdffaUjR47ob3/7W43eD5UqQ1JYWJhbe+X1SacvkZGRZ9xWp06dJEn79u2rts8PP/wgSQoPD3e13Xnnndq6dau++eYbSdKKFSvkdDp16623uvr8+OOP+vLLL11BrXK54IILZIxxm66Uqn5fVcWb99r999+vo0ePuj5t9cILL6hjx476z//8zxrtC6gtOz+uAJwjPz8/JSYmKjExUUeOHNGGDRv08MMPa+TIkTpw4MAZP57aunVrSVJeXp7Hx2YPHTqkNm3auPX78ccfPbaRn59f5VmXyr+8T/e3v/1NQ4YM0eLFi93ajx49euYnWUcGDBigVq1aacOGDfrhhx80bNgwORwODRs2TAsWLND27duVm5t7zsHlXFWGi3Oxbt06SXK7cLq2RowYoaVLl2rt2rWaPXt2lX3Wrl0rPz8/t/3deuutSkxM1MqVK/XEE0/olVde0bhx49zOmLRp00ZBQUFavnx5ldutfA9Wqup9VRVv3muXXnqpRo0apYULF2rUqFFat26dUlJS5OvrW6N9AbXFGRc0exdeeKFuvvlm3XvvvTp8+LDrr2Cn0ylJHn9pDh06VNKp/+RPt337duXk5GjYsGGSTh3wnU6n0tPT3fpt27atxtMf0qmDTmUtlb788ktt3bq1xts4F/7+/rrmmmuUmZmpjz76SCNGjJAkDRo0SH5+fnrkkUdcQeZMqns9zxeZmZlatmyZYmNjazTdeDY33nijevbsqT//+c9VXoydnp6u9evXa+rUqWrXrp2r/aKLLtK4ceP08ssv65133lF+fr7bNJF06iaL33//vVq3bl3lWcfqpiLPxtv32vTp0/Xll19q4sSJ8vX11V133VWr/QLe4IwLmqUxY8aoV69eiomJ0SWXXKL9+/frmWeeUUREhOs6jd/97neSpGeffVYTJ06Uv7+/unfvru7du+sPf/iDnn/+efn4+GjUqFH64Ycf9Kc//Unh4eGaOXOmpFNTM4mJiUpNTdVFF12kG2+8UQcPHlRKSorat2/vdh3Kmdxwww167LHHNGfOHA0ePFj/+te/NG/ePEVGRurkyZP18wL9xrBhwzRr1ixJcp1ZCQoKUmxsrNavX6/evXurbdu2Z9xG165dFRQUpFWrVikqKkqtWrVSWFiYx7RMfauoqHDdp6W0tFS5ubl677339PrrrysqKkqvv/56nezH19dXq1ev1ogRIzRw4EDNmjVLAwcOVGlpqf7+979r6dKlGjx4sBYsWOCx7p133qn09HTdd9996tixo8fZrBkzZmj16tW65pprNHPmTPXu3VsVFRXKzc3V+vXrNWvWLA0YMMDrmr19r40YMUI9e/bUxo0b9fvf//6s7wGgLhBc0Cxde+21Wr16tZYtW6aSkhK1a9dOI0aM0J/+9CfXjcqGDBmipKQkvfTSS3rxxRdVUVGhjRs3uk6ld+3aVWlpaVq4cKFCQkJ03XXXKTU11TVFJElPPPGEWrZsqSVLlmjFihXq0aOHFi9erOTk5BrfjTc5OVnHjh1TWlqa5s+fr549e2rJkiVas2ZNlR+Hrg+VB85u3bopIiLCrX3jxo01miZq0aKFli9frpSUFMXFxamsrExz5sxp8FvOHz9+XAMHDpR0Knxdcskl6tOnj1588UXdfvvtrmt/6kKPHj20a9cu/eUvf9Err7yixx57TH5+furZs6eeeeYZ/eEPf3C93043fPhwhYeH68CBA0pOTvYIuS1btlRWVpb+/Oc/a+nSpdq3b5+CgoLUqVMnDR8+vNZnXGrzXhs/frzmzp3LRbloMA5T3WX0AOrFvn371KNHD82ZM0cPP/xwY5cDnJOYmBiPmxQC9YkzLkA9+uKLL/Taa68pNjZWwcHB+te//qX58+crODhYU6ZMaezygFopKSnRV199pXfeeUc7d+7UmjVrGrskNCMEF6AetWzZUjt27FBaWpqOHDmikJAQDRkyRE888US1H4kGznf/+Mc/dO2116p169aaM2fOGe8ODNQ1pooAAIA1vP449CeffKIxY8YoLCxMDodDa9euPes6mzZtUnR0tAIDA9WlS5cG/SZUAADQdHgdXH755Rf16dNHL7zwQo3679u3T6NHj9agQYOUnZ2thx9+WNOmTdPq1au9LhYAADRv5zRV5HA4tGbNmjPObz700ENat26d2/dcJCQk6IsvvmiwG2gBAICmod4vzt26davi4uLc2kaOHKm0tDSVlZVVeQ+D0tJSlZaWuh5XVFTo8OHDat26dY1vXQ0AABqXMUZHjx5VWFhYjW+6eTb1Hlzy8/M9Pj0RGhqqkydPqrCwsMov/0pNTVVKSkp9lwYAABrAgQMHPL7brbYa5OPQvz1L8tuvcv+tpKQkJSYmuh4XFxerU6dOOnDggIKDg+uvUAAAUGdKSkoUHh6uCy64oM62We/BpV27dsrPz3drKygokJ+fn9ut0U/ndDo9vuhLkoKDgwkuAABYpi4v86j3b4ceOHCgMjMz3drWr1+vmJiYKq9vAQAAqI7XweXnn3/Wrl27tGvXLkmnPu68a9cu5ebmSjo1zTNhwgRX/4SEBO3fv1+JiYnKycnR8uXLlZaWpgceeKBungEAAGg2vJ4q2rFjh6699lrX48prUSZOnKiVK1cqLy/PFWIkKTIyUhkZGZo5c6YWLlyosLAwPffcc7rpppvqoHwAANCcWHHL/5KSEoWEhKi4uJhrXAAAsER9HL/r/RoXAACAukJwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALBGrYLLokWLFBkZqcDAQEVHRysrK+uM/VetWqU+ffqoRYsWat++vSZPnqyioqJaFQwAAJovr4NLenq6ZsyYoeTkZGVnZ2vQoEEaNWqUcnNzq+z/6aefasKECZoyZYq+/vprvfHGG9q+fbumTp16zsUDAIDmxevg8vTTT2vKlCmaOnWqoqKi9Mwzzyg8PFyLFy+usv+2bdvUuXNnTZs2TZGRkbr66qv1xz/+UTt27Djn4gEAQPPiVXA5ceKEdu7cqbi4OLf2uLg4bdmypcp1YmNjdfDgQWVkZMgYox9//FFvvvmmrr/++mr3U1paqpKSErcFAADAq+BSWFio8vJyhYaGurWHhoYqPz+/ynViY2O1atUqxcfHKyAgQO3atdOFF16o559/vtr9pKamKiQkxLWEh4d7UyYAAGiianVxrsPhcHtsjPFoq7R7925NmzZNjz76qHbu3Kn3339f+/btU0JCQrXbT0pKUnFxsWs5cOBAbcoEAABNjJ83ndu0aSNfX1+PsysFBQUeZ2Eqpaam6qqrrtKDDz4oSerdu7datmypQYMG6fHHH1f79u091nE6nXI6nd6UBgAAmgGvzrgEBAQoOjpamZmZbu2ZmZmKjY2tcp1jx47Jx8d9N76+vpJOnakBAACoKa+nihITE7Vs2TItX75cOTk5mjlzpnJzc11TP0lJSZowYYKr/5gxY/TWW29p8eLF2rt3rzZv3qxp06apf//+CgsLq7tnAgAAmjyvpookKT4+XkVFRZo3b57y8vLUq1cvZWRkKCIiQpKUl5fndk+XSZMm6ejRo3rhhRc0a9YsXXjhhRo6dKiefPLJunsWAACgWXAYC+ZrSkpKFBISouLiYgUHBzd2OQAAoAbq4/jNdxUBAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArFGr4LJo0SJFRkYqMDBQ0dHRysrKOmP/0tJSJScnKyIiQk6nU127dtXy5ctrVTAAAGi+/LxdIT09XTNmzNCiRYt01VVX6a9//atGjRql3bt3q1OnTlWuM378eP34449KS0vTpZdeqoKCAp08efKciwcAAM2LwxhjvFlhwIAB6tevnxYvXuxqi4qK0rhx45SamurR//3339ctt9yivXv36uKLL65VkSUlJQoJCVFxcbGCg4NrtQ0AANCw6uP47dVU0YkTJ7Rz507FxcW5tcfFxWnLli1VrrNu3TrFxMRo/vz56tChgy677DI98MADOn78eLX7KS0tVUlJidsCAADg1VRRYWGhysvLFRoa6tYeGhqq/Pz8KtfZu3evPv30UwUGBmrNmjUqLCzUPffco8OHD1d7nUtqaqpSUlK8KQ0AADQDtbo41+FwuD02xni0VaqoqJDD4dCqVavUv39/jR49Wk8//bRWrlxZ7VmXpKQkFRcXu5YDBw7UpkwAANDEeHXGpU2bNvL19fU4u1JQUOBxFqZS+/bt1aFDB4WEhLjaoqKiZIzRwYMH1a1bN491nE6nnE6nN6UBAIBmwKszLgEBAYqOjlZmZqZbe2ZmpmJjY6tc56qrrtKhQ4f0888/u9r27NkjHx8fdezYsRYlAwCA5srrqaLExEQtW7ZMy5cvV05OjmbOnKnc3FwlJCRIOjXNM2HCBFf/2267Ta1bt9bkyZO1e/duffLJJ3rwwQd15513KigoqO6eCQAAaPK8vo9LfHy8ioqKNG/ePOXl5alXr17KyMhQRESEJCkvL0+5ubmu/q1atVJmZqbuv/9+xcTEqHXr1ho/frwef/zxunsWAACgWfD6Pi6Ngfu4AABgn0a/jwsAAEBjIrgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWKNWwWXRokWKjIxUYGCgoqOjlZWVVaP1Nm/eLD8/P/Xt27c2uwUAAM2c18ElPT1dM2bMUHJysrKzszVo0CCNGjVKubm5Z1yvuLhYEyZM0LBhw2pdLAAAaN4cxhjjzQoDBgxQv379tHjxYldbVFSUxo0bp9TU1GrXu+WWW9StWzf5+vpq7dq12rVrV7V9S0tLVVpa6npcUlKi8PBwFRcXKzg42JtyAQBAIykpKVFISEidHr+9OuNy4sQJ7dy5U3FxcW7tcXFx2rJlS7XrrVixQt9//73mzJlTo/2kpqYqJCTEtYSHh3tTJgAAaKK8Ci6FhYUqLy9XaGioW3toaKjy8/OrXOfbb7/V7NmztWrVKvn5+dVoP0lJSSouLnYtBw4c8KZMAADQRNUsSfyGw+Fwe2yM8WiTpPLyct12221KSUnRZZddVuPtO51OOZ3O2pQGAACaMK+CS5s2beTr6+txdqWgoMDjLIwkHT16VDt27FB2drbuu+8+SVJFRYWMMfLz89P69es1dOjQcygfAAA0J15NFQUEBCg6OlqZmZlu7ZmZmYqNjfXoHxwcrH/+85/atWuXa0lISFD37t21a9cuDRgw4NyqBwAAzYrXU0WJiYm64447FBMTo4EDB2rp0qXKzc1VQkKCpFPXp/z73//Wyy+/LB8fH/Xq1ctt/bZt2yowMNCjHQAA4Gy8Di7x8fEqKirSvHnzlJeXp169eikjI0MRERGSpLy8vLPe0wUAAKA2vL6PS2Ooj8+BAwCA+tXo93EBAABoTAQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGvUKrgsWrRIkZGRCgwMVHR0tLKysqrt+9Zbb2nEiBG65JJLFBwcrIEDB+qDDz6odcEAAKD58jq4pKena8aMGUpOTlZ2drYGDRqkUaNGKTc3t8r+n3zyiUaMGKGMjAzt3LlT1157rcaMGaPs7OxzLh4AADQvDmOM8WaFAQMGqF+/flq8eLGrLSoqSuPGjVNqamqNtnH55ZcrPj5ejz76aJU/Ly0tVWlpqetxSUmJwsPDVVxcrODgYG/KBQAAjaSkpEQhISF1evz26ozLiRMntHPnTsXFxbm1x8XFacuWLTXaRkVFhY4ePaqLL7642j6pqakKCQlxLeHh4d6UCQAAmiivgkthYaHKy8sVGhrq1h4aGqr8/PwabWPBggX65ZdfNH78+Gr7JCUlqbi42LUcOHDAmzIBAEAT5VeblRwOh9tjY4xHW1Vee+01zZ07V2+//bbatm1bbT+n0ymn01mb0gAAQBPmVXBp06aNfH19Pc6uFBQUeJyF+a309HRNmTJFb7zxhoYPH+59pQAAoNnzaqooICBA0dHRyszMdGvPzMxUbGxsteu99tprmjRpkl599VVdf/31tasUAAA0e15PFSUmJuqOO+5QTEyMBg4cqKVLlyo3N1cJCQmSTl2f8u9//1svv/yypFOhZcKECXr22Wd15ZVXus7WBAUFKSQkpA6fCgAAaOq8Di7x8fEqKirSvHnzlJeXp169eikjI0MRERGSpLy8PLd7uvz1r3/VyZMnde+99+ree+91tU+cOFErV64892cAAACaDa/v49IY6uNz4AAAoH41+n1cAAAAGhPBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1ahVcFi1apMjISAUGBio6OlpZWVln7L9p0yZFR0crMDBQXbp00ZIlS2pVLAAAaN68Di7p6emaMWOGkpOTlZ2drUGDBmnUqFHKzc2tsv++ffs0evRoDRo0SNnZ2Xr44Yc1bdo0rV69+pyLBwAAzYvDGGO8WWHAgAHq16+fFi9e7GqLiorSuHHjlJqa6tH/oYce0rp165STk+NqS0hI0BdffKGtW7fWaJ8lJSUKCQlRcXGxgoODvSkXAAA0kvo4fvt50/nEiRPauXOnZs+e7dYeFxenLVu2VLnO1q1bFRcX59Y2cuRIpaWlqaysTP7+/h7rlJaWqrS01PW4uLhY0qkXAAAA2KHyuO3lOZIz8iq4FBYWqry8XKGhoW7toaGhys/Pr3Kd/Pz8KvufPHlShYWFat++vcc6qampSklJ8WgPDw/3plwAAHAeKCoqUkhISJ1sy6vgUsnhcLg9NsZ4tJ2tf1XtlZKSkpSYmOh6fOTIEUVERCg3N7fOnjhqp6SkROHh4Tpw4ADTdo2MsTh/MBbnF8bj/FFcXKxOnTrp4osvrrNtehVc2rRpI19fX4+zKwUFBR5nVSq1a9euyv5+fn5q3bp1les4nU45nU6P9pCQEN6E54ng4GDG4jzBWJw/GIvzC+Nx/vDxqbu7r3i1pYCAAEVHRyszM9OtPTMzU7GxsVWuM3DgQI/+69evV0xMTJXXtwAAAFTH6wiUmJioZcuWafny5crJydHMmTOVm5urhIQESaemeSZMmODqn5CQoP379ysxMVE5OTlavny50tLS9MADD9TdswAAAM2C19e4xMfHq6ioSPPmzVNeXp569eqljIwMRURESJLy8vLc7ukSGRmpjIwMzZw5UwsXLlRYWJiee+453XTTTTXep9Pp1Jw5c6qcPkLDYizOH4zF+YOxOL8wHueP+hgLr+/jAgAA0Fj4riIAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANY4b4LLokWLFBkZqcDAQEVHRysrK+uM/Tdt2qTo6GgFBgaqS5cuWrJkSQNV2vR5MxZvvfWWRowYoUsuuUTBwcEaOHCgPvjggwastmnz9vei0ubNm+Xn56e+ffvWb4HNiLdjUVpaquTkZEVERMjpdKpr165avnx5A1XbtHk7FqtWrVKfPn3UokULtW/fXpMnT1ZRUVEDVdt0ffLJJxozZozCwsLkcDi0du3as65TJ8ducx74v//7P+Pv729efPFFs3v3bjN9+nTTsmVLs3///ir7792717Ro0cJMnz7d7N6927z44ovG39/fvPnmmw1cedPj7VhMnz7dPPnkk+bzzz83e/bsMUlJScbf39/84x//aODKmx5vx6LSkSNHTJcuXUxcXJzp06dPwxTbxNVmLMaOHWsGDBhgMjMzzb59+8xnn31mNm/e3IBVN03ejkVWVpbx8fExzz77rNm7d6/Jysoyl19+uRk3blwDV970ZGRkmOTkZLN69WojyaxZs+aM/evq2H1eBJf+/fubhIQEt7YePXqY2bNnV9n/v//7v02PHj3c2v74xz+aK6+8st5qbC68HYuq9OzZ06SkpNR1ac1ObcciPj7ePPLII2bOnDkElzri7Vi89957JiQkxBQVFTVEec2Kt2Px1FNPmS5duri1Pffcc6Zjx471VmNzVJPgUlfH7kafKjpx4oR27typuLg4t/a4uDht2bKlynW2bt3q0X/kyJHasWOHysrK6q3Wpq42Y/FbFRUVOnr0aJ1+E2hzVNuxWLFihb7//nvNmTOnvktsNmozFuvWrVNMTIzmz5+vDh066LLLLtMDDzyg48ePN0TJTVZtxiI2NlYHDx5URkaGjDH68ccf9eabb+r6669viJJxmro6dnt9y/+6VlhYqPLyco9vlw4NDfX4VulK+fn5VfY/efKkCgsL1b59+3qrtymrzVj81oIFC/TLL79o/Pjx9VFis1Gbsfj22281e/ZsZWVlyc+v0X+1m4zajMXevXv16aefKjAwUGvWrFFhYaHuueceHT58mOtczkFtxiI2NlarVq1SfHy8fv31V508eVJjx47V888/3xAl4zR1dexu9DMulRwOh9tjY4xH29n6V9UO73k7FpVee+01zZ07V+np6Wrbtm19ldes1HQsysvLddtttyklJUWXXXZZQ5XXrHjze1FRUSGHw6FVq1apf//+Gj16tJ5++mmtXLmSsy51wJux2L17t6ZNm6ZHH31UO3fu1Pvvv699+/a5vhgYDasujt2N/mdZmzZt5Ovr65GWCwoKPJJZpXbt2lXZ38/PT61bt663Wpu62oxFpfT0dE2ZMkVvvPGGhg8fXp9lNgvejsXRo0e1Y8cOZWdn67777pN06uBpjJGfn5/Wr1+voUOHNkjtTU1tfi/at2+vDh06KCQkxNUWFRUlY4wOHjyobt261WvNTVVtxiI1NVVXXXWVHnzwQUlS79691bJlSw0aNEiPP/44Z+gbUF0duxv9jEtAQICio6OVmZnp1p6ZmanY2Ngq1xk4cKBH//Xr1ysmJkb+/v71VmtTV5uxkE6daZk0aZJeffVV5o3riLdjERwcrH/+85/atWuXa0lISFD37t21a9cuDRgwoKFKb3Jq83tx1VVX6dChQ/r5559dbXv27JGPj486duxYr/U2ZbUZi2PHjsnHx/1Q5+vrK+n//7WPhlFnx26vLuWtJ5Ufb0tLSzO7d+82M2bMMC1btjQ//PCDMcaY2bNnmzvuuMPVv/IjVTNnzjS7d+82aWlpfBy6jng7Fq+++qrx8/MzCxcuNHl5ea7lyJEjjfUUmgxvx+K3+FRR3fF2LI4ePWo6duxobr75ZvP111+bTZs2mW7dupmpU6c21lNoMrwdixUrVhg/Pz+zaNEi8/3335tPP/3UxMTEmP79+zfWU2gyjh49arKzs012draRZJ5++mmTnZ3t+mh6fR27z4vgYowxCxcuNBERESYgIMD069fPbNq0yfWziRMnmsGDB7v1//jjj80VV1xhAgICTOfOnc3ixYsbuOKmy5uxGDx4sJHksUycOLHhC2+CvP29OB3BpW55OxY5OTlm+PDhJigoyHTs2NEkJiaaY8eONXDVTZO3Y/Hcc8+Znj17mqCgINO+fXtz++23m4MHDzZw1U3Pxo0bz/j/f30dux3GcK4MAADYodGvcQEAAKgpggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWOP/AffH24v9EGeJAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.title('Histogram with PDF Overlay')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2705fcc1-6ed5-4666-abd2-cd9bf37b74c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1e0cf6fc-d79c-40c6-9308-712968d69840",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QUESTION17"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b51c0d3-5ff8-4199-b9cf-e3c6f06c4dd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a Seaborn scatter plot of two random arrays, color points based on their position relative to the\n",
    "#origin (quadrants), add a legend, label the axes, and set the title as 'Quadrant-wise Scatter Plot'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8c275f2b-1f4f-457f-bbe1-0d6e5f991a45",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "# Generate two random arrays\n",
    "x = np.random.randn(100)\n",
    "y = np.random.randn(100)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8e3e392f-a5dd-44d2-bd99-2b27d58a370a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Determine quadrant for each point\n",
    "quadrant = np.zeros(100)\n",
    "quadrant[(x > 0) & (y > 0)] = 1 \n",
    "quadrant[(x < 0) & (y > 0)] = 2\n",
    "quadrant[(x < 0) & (y < 0)] = 3\n",
    "quadrant[(x > 0) & (y < 0)] = 4  \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "372672aa-22ae-466e-bb19-fc9403263c11",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a DataFrame for Seaborn plotting\n",
    "data = {'x': x, 'y': y, 'Quadrant': quadrant}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Define color palette for each quadrant\n",
    "palette = {1: 'blue', 2: 'green', 3: 'orange', 4: 'red'}\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2cdfb094-f93b-417f-bf21-088239e04ad5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot: xlabel='x', ylabel='y'>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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SknNXyoqKqoSmujoaFeH0+gF//XTVHZ2NrGxsVqKKtoFWfNh+4cmoTl1BDTpBsFxro5MxL3Ex5vTnIcMgaNLPqOi4O23Qf8+Sy2U1PzlcA1NSIh+wq6rw+9VWVmZdyc1RWnw44VQsOXItYw5kPx36PEqBMW6LjZ3sHs3/PILfPWV2XE0ZAgkJ+tcEm8VHAwDB8LatfDmm7B1K1x4IQweDK1auTo6aeSU1BxDS051p/cKqCiDLW9WT2gOS/sMTr1fSU1tdu40H1hbtx659r//weuvw803m0PXxPuEhUGnTjBxoumQHhTk6ojETeicGpGTUZoDW9+1P775DbBWOi8ed3LwIIwbVz2hOey++yAjw+khSSPj66uERupFSY2bGDduHF27dnV1GFKDFazl9ocry6rXBcgROTnwySf2x+fOdV4sIuIRlNTUw65duxg6dCiJiYkEBATQsmVLRo4cyd69e10dWoNSAlUPgTGQfJ398TZDwceL641qU1Fhe4fLYfv3Oy8WEfEISmrqaNu2bfTo0YM///yTadOmsWXLFt544w1++OEHevXqxb59+1wa36HaPhzEcXwDof1DtutmmvWGJl2cH5O7iIiAs86yPz5ggPNiERGPoKSmju6//34CAgKYN28e559/PsnJyQwYMIDvv/+e9PR0xo4dC5ji2a+++qrac6Oiopg6dWrV14888ginnnoqISEhtG7dmn/96181TjCeMGECcXFxhIeHM3ToUEpKSqqN33bbbQwaNIjx48eTmJjIqaeeCsBHH31Ejx49CA8PJz4+nhtvvLHqPBmAhQsXYrFY+OGHH+jRowchISGcc845bNq0CYCpU6fy1FNPsWbNGiwWCxaLpVrsYkNYCvRfDh3HQHhbiOoMPd+Cc6dDsM7wsSs6Gl55Bfxs7Fe48ELtdBGRelNSUwf79u3ju+++47777qs6n+Ww+Ph4brrpJj799FPq2kYrPDycqVOnsmHDBl5++WXeeustXnrpparxzz77jCeffJJ///vfpKamkpCQwOuvv17jdX744Qc2btzI/PnzmT17NmBmbJ555hnWrFnDV199xfbt27nttttqPHfs2LG88MILpKam4ufnxx133AHAddddx0MPPUTHjh3JzMwkMzOT666rZXlFjLAU6DQOLloCF3wPbe+EEDVEPK7OnWHFCrjkEnPgWkIC/Pe/8MEH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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create the scatter plot\n",
    "sns.scatterplot(data=df, x='x', y='y', hue='Quadrant', palette=palette)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "915a7cb7-65c1-469e-8a52-37c734ca34f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7f8c4116cbb0>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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UrVqVZ577jnmzZvHyZMnWbJkCVlZWYVTZQXTesamKAuMGzeON954g759+/L777/z999/s3v3bpo0aVKi97Q458+fR9M0goKCinyvO3fuJCUlRe/625naWb9+Pbt37+bAgQOkpKTw559/Ur9+faPXF/zcGnqt0NBQvWlCIUxB1tQIcQN7e3u6dOnCqlWriI2NNfihFRsby969e+nZs2dhm4uLC9nZ2UWuvfmD5ddffyUjI4OlS5fqjbjcvJW3ILko+LC+UWJiosFFyYZGjb777js6derE7Nmz9dqvXLlS5No7NWnSJEaNGlV439PTs/Drrl278sYbb7B161Y2bNjAxIkTC9vXrl1buNOouPUuoJLOadOmMW3aNKKjo1m+fDmvvvoqSUlJrF69unCnzmeffWZ059SN60xK6uGHH2bKlCn8888/wPU1JbGxscU+rmB9z3vvvafXnpKSgo+PT6njuJG/vz86nY5t27YVJp83urntdkYVmzRpUvielkTBz21CQkKRvvj4+FI9lxC3Q0ZqhLjJq6++iqZpjBgxQm/HDqiFxM899xx5eXmMGTOmsL1atWokJSUVjhQAXLt2jTVr1ug9vuCD5cYPHE3T+PLLL/Wua926NS4uLnz//fd67du3by/RVNCNr3fzh9uhQ4f0FmeWlrHRm2rVqtGiRYvC242LmVu2bImXlxfTpk0jMTGR7t27A2oEZ//+/fz444/Ur1+f0NDQEscRHh7OqFGj6N69O/v27QOgbdu2+Pj4cPToUb1Ybrw5OTkZfU5DH8YA6enpxMTEFMZXu3ZtatSowfz58w0mswUMvf9//PEHcXFxem3FjYgZ67vvvvvQNI24uDiD32ejRo2MxmUqkZGRuLq68t133+m1x8bGsnHjRr2ktTSjgEKUlIzUCHGTtm3bMm3aNMaMGUO7du0YNWoU4eHhREdHM2vWLHbs2MGkSZMKP5gBHnnkEd58800effRRXnrpJbKyspgxY0aRpKh79+44OTkxYMAAXn75ZbKyspg9ezaXLl3Su65SpUr873//45133mHo0KE89NBDxMTEMGnSJKPTT4bcd999vP3220ycOJGOHTty/Phx3nrrLSIiIsjNzb2t96fgw/KDDz6gV69e2Nvb07hx42KTBXt7ezp27Mjvv/9OREQENWrUANR77ezszIYNG3j++eeLfd3U1FQ6d+7M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8fXXX9OoUSNmzJjBmDFjGD58OEFBQUyaNMng840cOZJr166xdetW3N3dOXr0qFRlF8JKyfSTEMLi/v33X+rVq0ejRo3Yt28fDg4l/3vro48+YsmSJezZs6ew7aeffmLgwIGMGzeO6dOns3//fmrXrg2okZrOnTtz6dIlfHx8aNy4Mf3792fixIll/n0JIcxLpp+EEBY3f/583NzciIqKIjY2FoDhw4fj4eFReCvw888/065dO4KDg/Hw8OCNN94gOjpa7/keeugh+vXrx5QpU/j4448LExpDnn/+ed555x3atm3LxIkTOXTokGm+SSGEyUlSI4SwqB07dvDpp5/y22+/ERkZyZAhQ9A0jbfeeosDBw4U3gB27tzJo48+Sq9evVixYgX79+9nwoQJXLt2Te85MzMz2bt3L/b29pw8ebLY1x86dChnzpxh4MCBHD58mBYtWvDZZ5+Z6tsVQpiQJDVCCIu5evUqgwcP5tlnn6Vbt2589dVX7N69my+++ILAwEBq1qxZeAP466+/qFq1KhMmTKBFixbUqlWLc+fOFXneF198ETs7O1atWsWMGTPYuHFjsXGEhYUxfPhwli5dyosvvsiXX35pku9XCGFaktQIISzm1VdfJT8/nw8++ACA8PBwPv74Y1566SXOnj1b5PqaNWsSHR3N4sWLOX36NDNmzGDZsmV61/zxxx/Mnz+f77//nu7du/Pqq68yePBgLl26ZDCGsWPHsmbNGqKioti3bx8bN26kXr16Zf69CiFMTxYKCyEsYsuWLXTt2pXNmzfTrl07vb577rmH3Nxc1q9fj06n0+t7+eWXmT9/PtnZ2fTu3ZvWrVszadIkLl++THJyMo0aNWLMmDG89tprAOTm5tK2bVuqVavGkiVLiiwUHj16NKtWrSI2NhYvLy969uzJp59+ip+fn9neCyFE2ZCkRgghhBA2QaafhBBCCGETJKkRQgghhE2QpEYIIYQQNkGSGiGEEELYBElqhBBCCGETJKkRQgghhE2QpEYIIYQQNkGSGiGEEELYBElqhBBCCGETJKkRQgghhE2QpEYIIYQQNkGSGiGEEELYhP8H6YSYHV9G9DAAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "# Create the scatter plot\n",
    "sns.scatterplot(data=df, x='x', y='y', hue='Quadrant', palette=palette)\n",
    "\n",
    "# Label the axes and set the title\n",
    "plt.xlabel('X-axis')\n",
    "plt.ylabel('Y-axis')\n",
    "plt.title('Quadrant-wise Scatter Plot')\n",
    "\n",
    "# Show legend\n",
    "plt.legend(title='Quadrant')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb0565d1-6c98-443f-86ca-bb082e459866",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
