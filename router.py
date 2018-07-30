import connect
import test007_list_router
import test008_create_router
import test009_delete_router

try:
    c = connect.create_connection('http://127.0.0.1/identity', 'admin', 'admin', 'secret', 'RegionOne', 'default', 'default')

    while True:
        print("\r\n---Manage Routers----------------------------------")
        print("Select one of the following option:")
        print("Select 1 to List Routers\r\nSelect 2 to Create Routers\r\nSelect 3 to Delete Routers\r\nSelect 0 to Exit\r\n")
        while True:
            try:
                selection = int(raw_input("Your input: "))
            except ValueError:
                print("Please select one of the option.")
                continue
            else:
                break

        if selection == 0:
            print("Exit Program.")
            exit()
        elif selection == 1:
            list_inst = test007_list_router.List()
            list_inst.list_router(c)
        elif selection == 2:
            create_inst = test008_create_router.Create()
            create_inst.create_router(c)
        elif selection == 3:
            delete_inst = test009_delete_router.Delete()
            delete_inst.delete_router(c)
except Exception as e:
    print("Error in code: " + str(e))
