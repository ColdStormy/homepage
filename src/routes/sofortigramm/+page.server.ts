import db from 'database.json';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	return {
		imageDatabase: db
	};
};