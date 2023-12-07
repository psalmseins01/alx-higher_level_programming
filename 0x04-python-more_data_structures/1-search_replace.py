#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def trace_element(elem):
        return elem if elem != search else replace
    return list(map(trace_element, my_list))
