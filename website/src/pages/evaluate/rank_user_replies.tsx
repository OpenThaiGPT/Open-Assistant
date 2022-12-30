import Head from "next/head";
import { useState } from "react";
import useSWRImmutable from "swr/immutable";
import useSWRMutation from "swr/mutation";

import fetcher from "src/lib/fetcher";
import poster from "src/lib/poster";

import { LoadingScreen } from "src/components/Loading/LoadingScreen";
import { Sortable } from "src/components/Sortable/Sortable";
import { TaskInfo } from "src/components/TaskInfo/TaskInfo";
import { Container, Flex, useColorModeValue } from "@chakra-ui/react";
import { SkipButton } from "src/components/Buttons/Skip";
import { SubmitButton } from "src/components/Buttons/Submit";

const RankUserReplies = () => {
  const [tasks, setTasks] = useState([]);
  /**
   * This array will contain the ranked indices of the replies
   * The best reply will have index 0, and the worst is the last.
   */
  const [ranking, setRanking] = useState<number[]>([]);
  const bg = useColorModeValue("gray.100", "gray.800");
  const { isLoading } = useSWRImmutable("/api/new_task/rank_user_replies", fetcher, {
    onSuccess: (data) => {
      setTasks([data]);
    },
  });

  const { trigger, isMutating } = useSWRMutation("/api/update_task", poster, {
    onSuccess: async (data) => {
      const newTask = await data.json();
      setTasks((oldTasks) => [...oldTasks, newTask]);
    },
  });

  const submitResponse = (task) => {
    trigger({
      id: task.id,
      update_type: "post_ranking",
      content: {
        ranking,
      },
    });
  };

  if (isLoading) {
    return <LoadingScreen text="Loading..." />;
  }

  if (tasks.length == 0) {
    return <Container className="p-6 bg-slate-100 text-gray-800">Loading...</Container>;
  }
  const replies = tasks[0].task.replies as string[];

  return (
    <>
      <Head>
        <title>Rank User Replies</title>
        <meta name="description" content="Rank User Replies." />
      </Head>
      <Container className="p-6 text-gray-800">
        <Container bg={bg} className="rounded-lg shadow-lg block bg-white p-6 mb-8">
          <h5 className="text-lg font-semibold mb-4">Instructions</h5>
          <p className="text-lg py-1">
            Given the following replies, sort them from best to worst, best being first, worst being last.
          </p>
          <Sortable items={replies} onChange={setRanking} />
        </Container>

        <section className="mb-8 p-4 rounded-lg shadow-lg bg-white flex flex-row justify-items-stretch ">
          <TaskInfo id={tasks[0].id} output="Submit your answer" />

          <Flex justify="center" ml="auto" gap={2}>
            <SkipButton>Skip</SkipButton>
            <SubmitButton onClick={() => submitResponse(tasks[0])} disabled={ranking.length === 0}>
              Submit
            </SubmitButton>
          </Flex>
        </section>
      </Container>
    </>
  );
};

export default RankUserReplies;
