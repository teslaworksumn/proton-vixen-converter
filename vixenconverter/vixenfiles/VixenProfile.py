import os

from vixenfiles import VixenFile, VixenException


class VixenProfile(VixenFile):
    def __init__(self, pro_path):
        super().__init__(pro_path)
        if self.get_type() != 'Profile':
            raise VixenException("File is not a Vixen profile")
        self.name = pro_path.split('/')[-1].split('.')[0]

    def get_output_order(self):
        order = self.root.find("Outputs").text
        return list(map(lambda x: int(x), order.split(',')))

    def get_channels(self):
        channels = self.root.find("ChannelObjects")
        output_order = self.get_output_order()
        pretty_channels = list(map(lambda channel: {
            'channelName': channel.text.replace('(', ' ').replace(')', ' ').replace('.', ' ').replace('\'', ' '),
            'color': format(int(channel.attrib['color']) & 0xffffff, "06X"),
            'dmxChannel': output_order.index(int(channel.attrib['output'])) + 1,
            'fixtureName': 'VixFix' + self.name,
            'location': '0,0,0',
            'rotation': '0,0,0'
        }, channels))
        return pretty_channels

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
