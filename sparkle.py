def halloween(back=orange, sc=purple, dee=.04, spark=5):
    while True:
        for i in range(spark):
            wan = random.randint(0,29)
            too = random.randint(0,29)
            tree = random.randint(0,29)
            np.fill(back)
            np[wan] = sc
            np[too] = sc
            np[tree] = sc
            np.show()
            time.sleep(dee)
        

halloween()

