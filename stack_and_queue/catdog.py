#!/usr/bin/env python  
# -*-coding: utf-8 -*- 

""" 
@Version:           v0.1
@Author:            tianbaorenjie
@License:           GPL Licence  
@Contact:           tianbaorenjie@163.com
@Site:              https://github.com/tianbaorenjie 
@Software:          PyCharm 
@Project:           py363_algorithm
@File:              catdog.py 
@Time:              17-11-29 下午7:28 
"""
"""
1.调用add方法将cat类或是dog类实例加入队列中
2.调用poll_all方法,将队列中所有实例按照进队列的先后顺序依次弹出
3.调用poll_dog方法将队列中dog类实例按照进队列先后顺序依次弹出
4.调用poll_cat方法将队列中cat类实例按照进队列先后顺序依次弹出
5.调用is_empty方法检查队列中是否还有cat或是dog实例
6.调用is_dog_empty检查队列中是否还有dog类实例
7.调用is_cat_empty检查队列中是否还有cat类实例
"""


class Pet:
    def __init__(self, ptype):
        self.__type = ptype

    def get_pet_type(self):
        return self.__type


class Dog(Pet):
    def __init__(self):
        super(Dog, self).__init__("dog")


class Cat(Pet):
    def __init__(self):
        super(Cat, self).__init__("cat")
# 以上为原始类,不能修改


class PetElement:
    """定义新类覆盖原始Pet类，添加__count标记时间戳"""
    __slots__ = ["__pet", "__count"]

    def __init__(self, pet, count):
        self.__pet = pet
        self.__count = count

    def __str__(self):
        return "<%s:%s>" % (self.__pet, self.__count)

    def get_pet(self):
        return self.__pet

    def get_count(self):
        return self.__count

    def get_element_pet_type(self):
        return self.__pet.get_pet_type()


class PetQueue:
    """定义本题要求的基本队列操作"""
    __slots__ = ["__queue"]

    def __init__(self):
        self.__queue = []

    def length(self):
        return len(self.__queue)

    def is_empty(self):
        return self.length() == 0

    def push(self, pet):
        self.__queue.append(pet)

    def peek(self):
        if self.is_empty:
            raise NotImplementedError("Queue is empty!")
        return self.__queue[0]

    def poll(self):
        if self.is_empty:
            raise NotImplementedError("Queue is empty!")
        result = self.__queue[0]
        self.__queue = self.__queue[1:]
        return result


class CatDogQueue:
    """完成本题7个需求"""
    __slots__ = ["__cat_queue", "__dog_queue", "__count"]

    def __init__(self):
        self.__cat_queue = PetQueue()
        self.__dog_queue = PetQueue()
        self.__count = 0

    def __add_count(self):
        self.__count = self.__count+1
        return self.__count

    def add(self, pet):
        if pet.get_pet_type() == "cat":
            self.__cat_queue.push(PetElement(pet, self.__add_count()))
        elif pet.get_pet_type() == "dog":
            self.__dog_queue.push(PetElement(pet, self.__add_count()))
        else:
            raise RuntimeError("pet not cat or dog!!!")

    def is_cat_empty(self):
        return self.__cat_queue.is_empty

    def is_dog_empty(self):
        return self.__dog_queue.is_empty

    def is_empty(self):
        return not self.is_dog_empty() and not self.is_cat_empty()

    def poll_all(self):
        if self.is_cat_empty() and self.is_dog_empty():
            raise RuntimeError("queue is empty!!!")
        result = []
        while not self.is_dog_empty() and not self.is_cat_empty():
            if self.__cat_queue.peek().get_count() < self.__dog_queue.peek().get_count():
                result.insert(self.__cat_queue.peek().get_count()-1, self.__cat_queue.poll().get_pet())
            else:
                result.insert(self.__dog_queue.peek().get_count() - 1, self.__dog_queue.poll().get_pet())
        while self.is_cat_empty():
            result.insert(self.__dog_queue.peek().get_count() - 1, self.__dog_queue.poll().get_pet())
        while self.is_dog_empty():
            result.insert(self.__cat_queue.peek().get_count() - 1, self.__cat_queue.poll().get_pet())
        return result

    def poll_cat(self):
        if not self.is_cat_empty():
            return self.__cat_queue.poll().get_pet()
        else:
            raise RuntimeError("cat queue is empty!!!")

    def poll_dog(self):
        if not self.is_dog_empty():
            return self.__dog_queue.poll().get_pet()
        else:
            raise RuntimeError("dog queue is empty!!!")
