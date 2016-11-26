import os

from vixenfiles import VixenFile, VixenException


class VixenProfile(VixenFile, object):
    def __init__(self, pro_path):
        super().__init__(pro_path)
        if self.get_type() != 'Profile':
            raise VixenException("File is not a Vixen profile")

    def get_output_order(self):
        order = self.root.find("Outputs").text
        return list(map(lambda x: int(x), order.split(',')))


    # Factory method to create a VixenProfile
    # Checks if file path/extension is valid
    # and builds sequence path from vix_path and file
    @staticmethod
    def make_vixen_profile(pro_path):
        if pro_path is None:
            raise VixenException("No path specified")

        if os.path.splitext(pro_path)[-1] != ".pro":
            raise ValueError("Not a .pro file")

        return VixenProfile(pro_path)
