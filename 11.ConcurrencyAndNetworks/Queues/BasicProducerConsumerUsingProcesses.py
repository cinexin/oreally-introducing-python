import multiprocessing as mp

def washer(dishes, dish_queue):
    for dish in dishes:
        print('Washing',dish,'dish')
        dish_queue.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print('Drying', dish, 'dish')
        dish_queue.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer,args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()

dishes = ['salad','bread','entree','dessert']
washer(dishes, dish_queue)
dish_queue.join()