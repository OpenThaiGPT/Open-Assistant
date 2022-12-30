export const TaskInfo = ({ id, output }: { id: string; output: any }) => {
  return (
    <div className="grid grid-cols-[min-content_auto] gap-x-2  ">
      <b>Prompt</b>
      <span>{id}</span>
      <b>Output</b>
      <span>{output}</span>
    </div>
  );
};
