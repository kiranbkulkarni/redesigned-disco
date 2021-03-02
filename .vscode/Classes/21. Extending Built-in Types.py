class Text(str):
    def duplicate(self):
        return self + self


class TrackList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


list = TrackList()
list.append("1")

text = Text("Pyton")
print(text.lower())
print(text.duplicate())
