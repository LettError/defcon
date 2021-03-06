from defcon.objects.base import BaseObject


class Features(BaseObject):

    """
    This object contais the test represening features in the font.

    **This object posts the following notifications:**

    ================  ====
    Name              Note
    ================  ====
    Features.Changed  Posted when the *dirty* attribute is set.
    ================  ====
    """

    changeNotificationName = "Features.Changed"
    beginUndoNotificationName = "Features.BeginUndo"
    endUndoNotificationName = "Features.EndUndo"
    beginRedoNotificationName = "Features.BeginRedo"
    endRedoNotificationName = "Features.EndRedo"

    def __init__(self):
        super(Features, self).__init__()
        self._dirty = False
        self._text = None

    def _set_text(self, value):
        if self._text == value:
            return
        self._text = value
        self.dirty = True

    def _get_text(self):
        return self._text

    text = property(_get_text, _set_text, doc="The raw feature text. Setting this posts a *Features.Changed* notification.")

