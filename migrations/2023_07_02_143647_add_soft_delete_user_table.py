from orator.migrations import Migration


class AddSoftDeleteUserTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
