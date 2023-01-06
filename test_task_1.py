"""Tests for task 1."""

from task_1 import ChildMoocher, Getter, HelicopterParent, RichParent, Setter


class TestHelicopterParent:
    """Test for sub-class registration."""

    def test_new_subclass(self):
        """The subclass should show in in the list."""

        class SubClass(HelicopterParent):
            pass

        assert SubClass in HelicopterParent.children


class TestGetter:
    """Tests for dynamic attributes."""

    def test_c_updates(self):
        """Ensure c updates when a or b are changed."""
        get = Getter(a=2, b=2)
        assert get.c == 4
        # ensure changing a also updates c
        get.a = 3
        assert get.c == 5
        # and b too
        get.b = 10
        assert get.c == 13


class TestSetter:
    """Test previous values stored."""

    def test_list_changes_size(self):
        """Ensure the logging list changes size."""
        set = Setter(a=10)
        assert len(set.old_values_of_a) == 0
        # now update a
        set.a = 12
        assert set.old_values_of_a == [10]
        # do it again
        set.a = 22
        assert set.old_values_of_a == [10, 12]


class TestSpoiledKids:
    """Test inheritance between rich parent and moocher child."""

    def sum_assets(self, obj):
        """Sum up asset value."""
        out = []
        for name in dir(obj):
            if name.startswith("assert_"):
                out.append(getattr(obj, name))
        return sum(out)

    def test_parent_get_net_worth(self):
        """Test that the parent networth is determined."""
        parent = RichParent()
        assert parent.get_net_worth() > 0
        assert parent.get_net_worth() == self.sum_assets(parent)

    def test_child_net_worth(self):
        """Ensure the child's net worth is calculated as expected."""
        child = ChildMoocher()
        parent = RichParent()
        assert child.get_net_worth() == parent.get_net_worth() / child.siblings
        # change siblings and it should still be true
        child.siblings = 12
        assert child.get_net_worth() == parent.get_net_worth() / child.siblings
        # but adding parent siblings shouldnt do anyting.
        parent.siblings = 3
        assert child.get_net_worth() == parent.get_net_worth() / child.siblings

    def test_child_networth_actually_calls_parent_net_worth(self, monkeypatch):
        """Test child.get_net_worth actually calls parent.get_net_worth."""
        state = {"call_count": 0}

        def instrument(func):
            def _new_func(self, *args, **kwargs):
                state["call_count"] += 1
                return func(*args, **kwargs)

            return _new_func

        monkeypatch.setattr(
            RichParent, "get_net_worth", instrument(RichParent.get_net_worth)
        )

        child = ChildMoocher()
        assert state["call_count"] == 0
        child.get_net_worth()
        assert state["call_count"] == 1
