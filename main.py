import random
import time


class Location:
    my_item = ""
    my_description = ""
    my_id = int
    text_prompt = ""
    exits = {}

    def __init__(self, id_: int, description: str, item: str, describe_in: str):
        self.exits = {}
        self.my_item = item
        self.my_description = description
        self.my_id = id_
        self.text_prompt = describe_in

    def add_exits(self, direction: str, location: int):
        self.exits[direction] = location

    def get_all_exits(self):
        return list(self.exits.keys())

    def get_exit_value(self, direction_char: str):
        return self.exits[direction_char]

    def dialog(self):
        return self.text_prompt

    def get_item(self):
        return self.my_item.upper()

    def get_description(self):
        return self.my_description


if __name__ == '__main__':

    game_map = {}
    game_map[0] = Location(0, "Theater entrance ⚅🎭⚅",
                           "Nothing", "How old is this theatre ? looks like it has been forsaken")
    # Start room
    # theater room, it has a box full of Fuel
    game_map[1] = Location(1, "The stage room", "Fuel",
                           "Seems like there is a box of fuel out there, i wonder if it's useful ?")
    # central room ,Room contains flashlights
    game_map[2] = Location(2,
                           "Central theatre room.",
                           "Light", "How huge these scars on the walls ╭( ๐_๐)╮ , must be the villain. Oh a Light !")
    # Restroom, Room with ax
    game_map[3] = Location(3, "Restroom 🚻", "Ax",
                           "What is this smell Ouugh ヽ(。_ °)ノ !!!! should i take this Ax with me")
    # administration, important documents about the villain
    game_map[4] = Location(4, "Theater administration", "Documents",
                           "why is it so gloomy here !? Documents ? oh these are the villain's information")
    # hidden room in the administration [closet with keys]
    game_map[5] = Location(5, "administration library shelves", "keys",
                           "Oh! A hidden door behind the library. Oh (∿°○° ) keys !! must be useful.")
    # meeting_room, has a sword
    game_map[6] = Location(6, "Used to be a meeting room, but now it's old and abandoned =/", "Dragon Sword",
                           "Oh finally the Dragon Sword")
    # Villain Room
    game_map[7] = Location(7, " The villain's room where he's asleep ᕮ◥▶‿‿◀◤ᕭ", "Villain's head",
                           "You villain ! let's get some fun now, i'm not here to talk !!!")

    # ------------------------------------------
    # adding exits
    game_map[0].add_exits("E", 1)
    game_map[0].add_exits("S", 2)
    # theater room exits
    game_map[1].add_exits("W", 0)

    # central room exits
    game_map[2].add_exits("N", 0)
    game_map[2].add_exits("W", 3)
    game_map[2].add_exits("E", 4)
    game_map[2].add_exits("S", 6)
    # Rest Room exits
    game_map[3].add_exits("E", 2)
    # administration
    game_map[4].add_exits("W", 2)
    game_map[4].add_exits("N", 5)

    # hidden room exits
    game_map[5].add_exits("S", 4)
    # meeting room exits
    game_map[6].add_exits("N", 2)
    game_map[6].add_exits("E", 7)

    # villain room exits
    game_map[7].add_exits("W", 6)

    bag = []

    smart_approach = ["KEYS", "DOCUMENTS", "AX", "FUEL", "LIGHT"]
    hard_approach = ["KEYS", "DRAGON SWORD", "FUEL", "LIGHT"]
    currentLoc = 0


    def exits_view(direct, description):
        print("[{}]: {}".format(direct, description))


    # print text with animation
    def tt(text, delay):
        for i in text:
            print(end=i)
            time.sleep(delay)
        return ""


    def kill_approach():
        # check if smart approach can e done
        check_smart = all(item in bag for item in smart_approach)
        # check if Hard approach can e done
        check_hard = all(item in bag for item in hard_approach)
        if check_hard and check_smart:
            return "BOTH"
        elif check_hard:
            return "HARD"
        elif check_smart:
            return "SMART"
        else:
            return "DUMB"


    def hard_choice():
        print(tt(game_map[currentLoc].dialog(), 0.1))
        print("MONSTER:", end=" ")
        print(tt("you are going to die !!", 0.1))
        print("You:   #:~[", end=" ")
        print(tt("Let's see ", 0.1))
        option = random.choice(["WIN", "LOSE"])

        print(tt("=====/\/\/\/\/\\/\/\/\/\=====", 0.5))

        if option == "WIN":
            print("MONSTER ／(x~x)＼ ", end=" ")
            print(tt("please ! i ask for forgiveness ", 0.1))
            print("You :", end=" ")
            print(tt("what about the people you darkened, you should take this ", 0.1))
            print(tt("o()xxxx[{::::::::::::::::::::::::::::::::::>", 0.5))
            print("MONSTER ／(x~x)＼ ", end=" ")
            print(tt("Nooo", 0.1))
        else:  # in case you lost out of risk
            print("MONSTER (๑òᗜó) ", end=" ")
            print(tt("This is why you shouldn't dare me again HA.HA.HA", 0.1))
            print(tt("GAME LOST", 0.1))


    def smart_choice():
        print(tt(game_map[currentLoc].dialog(), 0.1))
        print("MONSTER:", end=" ")
        print(tt("What ! you got the documents with you !!", 0.1))
        print("You :", end=" ")
        print(tt("that's right, now you are going to die", 0.1))
        print("BATTLE", end=" ")
        print(tt("=====/\/\/\/\/\\/\/\/\/\=====", 0.8))
        print("MONSTER ／(x~x)＼ ", end=" ")
        print(tt("Nooooooo  ", 0.1))
        print("YOU WON")


    while True:
        exits = game_map.get(currentLoc)

        print("---> You are in", exits.get_description())

        if currentLoc == 7:
            print(tt("-------------------------------", 0.1))
            available_approach = kill_approach()

            if available_approach == "BOTH":
                print(tt("You have reached the Villain room. your bag has been filled by all the available resources.",
                         0.1))
                print(tt("You can now choose between two approaches, either smart approach or the hard one", 0.1))
                print(tt("the hard approach would make it challenging", 0.1))
                print(tt("although the collected items, and your chances of winning would be less estimated", 0.1))
                # choose which approach to take
                user_approach = str(input("which approach you want to take ? (HARD / SMART)"))

                if user_approach.upper() == "HARD":
                    available_approach = "HARD"
                elif user_approach.upper() == "SMART":
                    available_approach = "SMART"
                else:
                    print("please choose one choice (HARD / SMART)")
                    pass

                print(available_approach)
                # ------------------- another if statement after "approach" has been set

                print(tt("-------------------------------", 0.1))
                if available_approach == "HARD":
                    hard_choice()
                    break
                else:
                    smart_choice()
                    break
            elif available_approach == "SMART":
                smart_choice()
                break
            elif available_approach == "HARD":
                hard_choice()
                break
            else:  # DUMB
                print("MONSTER:", end=" ")
                print("HA.HA.HA i see you not carrying anything useful !")
                print("You :", end=" ")
                print(tt("still i will fight (ง︡'-'︠)ง", 0.1))
                print("MONSTER:", end=" ")
                print(tt("Ψ(￣ ∀ ￣)Ψ", 0.1))
                print("You die :(")
                print("MONSTER: ¯ਊ¯ ", end=" ")
                print(tt("HA HA HA ...", 0.1))
                print(tt("GAME LOST", 0.1))
                break

        if not exits.get_item().upper() in bag:
            print(tt(exits.dialog(), 0.1))
            if not (exits.get_item() == game_map[0].get_item() or exits.get_item() == game_map[7].get_item()):
                print("")
                user_input = str(input("do you want to carry this item ? (Y/N)"))
                if user_input.upper() == "Y":
                    bag.append(exits.get_item())
                    print("[", exits.get_item(), "has been added to your inventory]")
                else:
                    print("you left", exits.get_item())
        else:
            print(tt("it was from here where i got the " + exits.get_item(), 0.1))

        print("available exits are : ")
        for door in exits.get_all_exits():
            exits_view(door, game_map.get(exits.get_exit_value(door)).get_description())

        user_choice = str(input())
        appropriate_choices = ["W", "S", "N", "E"]

        if user_choice.upper() in appropriate_choices:
            if currentLoc == 6 and user_choice.upper() == "E":
                print("my bag ", bag)
                if "KEYS" in bag:
                    currentLoc = exits.get_exit_value(user_choice.upper())
                else:
                    print("You need the keys to enter this room")
            else:
                currentLoc = exits.get_exit_value(user_choice.upper())
        elif user_choice.upper() == "Q":
            print("Game exit")
            break
        else:
            print("You cannot go in that direction")
            print("please, choose one of the directions: W, S, N, W or Q to quit")

    print(tt("END OF THE STORY", 0.1))
    print(tt("Made by Hanan Hammed and her imagination", 0.1))
