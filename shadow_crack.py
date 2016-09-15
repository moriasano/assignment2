""" This code cracks the password for a given user from the shadow file """
import utils


def shadow_crack(shadow_file, username):
    """
    Main logic flow for the shadow file crack
    :param shadow_file: the shadow file
    :param username: the username of the password to crack
    :return: the cracked password
    """
    user_line = None
    for line in open(shadow_file, 'r').readlines():
        if username in line:
            user_line = line
            break

    if user_line is None:
        print("User '%s' was not found" % username)
        return

    hash_alg, salt, hashed_pwd = user_line.split(":")[1].split("$")[1:]


if __name__ == '__main__':
    utils.welcome()
    shadow_path, username = utils.get_sc_params()