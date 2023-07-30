from orator.migrations import Migration


class CreateSaltColumnUserTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.string("salt").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
