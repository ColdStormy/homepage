import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
    return {
        post: {
            imageID: params.imageID
        }
    };
};