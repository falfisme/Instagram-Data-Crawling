# Get instance
import instaloader

def ambilfollowers(target):
    L = instaloader.Instaloader(max_connection_attempts=0)

    # Login or load session
    username = 'snuu_ngkass'
    password = 'wisnuaji98'
    L.login(username, password)        # (login)

    follow_list = [target]
    # Obtain profile metadata
    instagram_target = target
    profile = instaloader.Profile.from_username(L.context, instagram_target)
    #print(profile.get_followers())
    #count=1
    #file = open("instagram_followers.txt","w")
    for followee in profile.get_followers():
        username = followee.username
        follow_list.append(username)
        #follow_list.extend(username)
        #file.write(str(count) + ". " + username + "\n")
        #print(str(count) + ". " + username)
        #count = count + 1

    print("Follower " + target + " Berhasil Didapatkan")
    #file.close()
    return follow_list

